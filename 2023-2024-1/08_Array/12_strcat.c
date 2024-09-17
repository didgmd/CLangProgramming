#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <string.h>

int main() {

	char str1[30] = { "People's Republic of " };
	char str2[] = { "China" };
	strcat(str1, str2);
	printf("%s\n", str1);
	// printf("%s\n", strcat(str1, str2));


	return 0;
}