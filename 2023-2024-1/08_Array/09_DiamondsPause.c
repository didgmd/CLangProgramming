#include <stdio.h>
#include <stdlib.h>

int main() {

	char diamonds[5][5] = { 
		{' ', ' ', '*'},
		{' ', '*', ' ', '*'},
		{'*', ' ', ' ', ' ', '*'},
		{' ', '*', ' ', '*'},
		{' ', ' ', '*'}};

	for (int i = 0; i <= 4; i++) {
		for (int j = 0; j <= 4; j++) {
			printf("%c", diamonds[i][j]);
		}
		printf("\n");
	}

	system("pause");

	return 0;
}