// 由于Visual Studio认为scanf()不够安全，因此须添加如下prefix才能使用scanf()
#define _CRT_SECURE_NO_WARNINGS 1
#pragma warning(disable: 6031)

// Include the standard library
#include <stdio.h>	// Include the standard input/output library
#include <stdlib.h> // Include the standard library

// Generate calculator program that adds, subtracts, multiplies, and divides two numbers with different functions
// Make an infinite loop that asks the user for a number, then asks for another number, then asks for an operation, then does the operation
// If the operation is invalid, print an error message and quit the program
// If the operation is valid, print the result and continue the loop

// add function
float add(float a, float b)
{
	return a + b;
}

// subtract function
float subtract(float a, float b)
{
	return a - b;
}

// multiply function
float multiply(float a, float b)
{
	return a * b;
}

// divide function
float divide(float a, float b)
{
	return a / b;
}

// main function
int main()
{
	// Declare variables
	float a, b, result;
	char operation;

	// Infinite loop
	while (1)
	{
		// Ask for a number
		printf("Enter a number: ");
		scanf("%f", &a);

		// Ask for another number
		printf("Enter another number: ");
		scanf("%f", &b);

		// Ask for an operation
		printf("Enter an operation: ");
		scanf(" %c", &operation);

		// Check if the operation is valid
		if (operation == '+')
		{
			// Add the numbers
			result = add(a, b);
		}
		else if (operation == '-')
		{
			// Subtract the numbers
			result = subtract(a, b);
		}
		else if (operation == '*')
		{
			// Multiply the numbers
			result = multiply(a, b);
		}
		else if (operation == '/')
		{
			// Divide the numbers
			result = divide(a, b);
		}
		else
		{
			// Print an error message
			printf("Invalid operation, exit the program\n");

			// Quit the program
			exit(1);
		}

		// Print the result
		printf("Result: %f\n", result);
	}

	// Return 0
	//	return 0;
}
