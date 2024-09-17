#include <stdio.h>

int main() {
	char a[5] = "China";
	char b[6] = "China";

	for (int i = 0; i <= 4; i++) {
		printf("%c", a[i]);
	}

	printf("\n");

	printf("a: %s\n", a);
	printf("b: %s\n", b);

	return 0;
}