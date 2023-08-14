#include <stdio.h>

// A calculator program that adds, subtracts, multiplies, and divides two numbers with different functions
int main()
{
    // Declare variables
    int a, b, result;
    char operation;

    // Ask for a number
    printf("Enter a number: ");
    scanf_s("%d", &a);

    // Ask for another number
    printf("Enter another number: ");
    scanf_s("%d", &b);

    // Ask for an operation
    printf("Enter an operation: ");
    scanf_s(" %c", &operation, 1);

    // Check if the operation is valid
    if (operation == '+')
    {
        // Add the numbers
        result = a + b;
    }
    else if (operation == '-')
    {
        // Subtract the numbers
        result = a - b;
    }
    else if (operation == '*')
    {
        // Multiply the numbers
        result = a * b;
    }
    else if (operation == '/')
    {
        // Divide the numbers
        result = a / b;
    }
    else
    {
        // Print an error message
        printf("Invalid operation!\n");
        return 1;
    }

    // Print the result
    printf("Result: %d\n", result);

    return 0;
}
