#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>

int main() {

	FILE* fp;
	
	fp = fopen("test.txt", "w");
	if (fp == NULL) {
		printf("Cannot open file\n");
		exit(0);
	}

	printf("Please enter a string to store in the disk (end with #): ");
	char ch = getchar();	// Get the first char
	while (ch != '#') {		// When input is not '#'
		fputc(ch, fp);		// Write the first char to the file
		ch = getchar();		// Get the next char
	}
	fclose(fp);

	fp = fopen("test.txt", "r");
	if (fp == NULL) {
		printf("Cannot open file\n");
		exit(0);
	}

	printf("The content of the file is: ");
	ch = fgetc(fp);			// Get the first char
	while (ch != EOF) {		// When input is not EOF
		putchar(ch);		// Print the first char
		ch = fgetc(fp);		// Get the next char
	}
	fclose(fp);

	return 0;
}