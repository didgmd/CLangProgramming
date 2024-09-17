#include <stdio.h>

struct Student {
    char name[50];
    int id;
    float score;
};

void printStudentInfo(struct Student* s) {
    printf("Name: %s\n", s->name);
    printf("ID: %d\n", s->id);
    printf("Score: %.2f\n", s->score);
}

int main() {
    struct Student student1;
    struct Student* ptr = &student1;

    strcpy(student1.name, "Alice");
    student1.id = 12345;
    student1.score = 95.5;

    printStudentInfo(ptr);

    return 0;
}
