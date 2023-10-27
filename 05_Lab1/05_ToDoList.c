#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
#include <string.h>

void displayTasks(char tasks[][50], int n) {
    printf("To-Do List:\n");
    for (int i = 0; i < n; i++) {
        printf("%d. %s\n", i + 1, tasks[i]);
    }
}

int main() {
    char tasks[10][50];  // Array to store up to 10 tasks, each of a maximum length of 50 characters
    int n = 0;  // Number of tasks
    int choice;

    while (1) {
        printf("1. Add Task\n");
        printf("2. Complete Task\n");
        printf("3. Display Tasks\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("Enter the task: ");
            scanf(" %[^\n]", tasks[n]);  // Read a line of text
            n++;
        }
        else if (choice == 2) {
            int taskNumber;
            printf("Enter the task number to mark as complete: ");
            scanf("%d", &taskNumber);
            for (int i = taskNumber - 1; i < n - 1; i++) {
                strcpy(tasks[i], tasks[i + 1]);  // Shift tasks up
            }
            n--;  // Reduce the number of tasks
        }
        else if (choice == 3) {
            displayTasks(tasks, n);
        }
        else if (choice == 4) {
            break;
        }
        else {
            printf("Invalid choice. Try again.\n");
        }
    }

    return 0;
}
