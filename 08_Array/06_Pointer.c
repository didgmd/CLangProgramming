#include <stdio.h>

int main() {
	int a[5] = { 1, 2, 3, 4, 5 };

	// 取址符 &
	// 输出数组 a 中所有元素的首地址
	printf("a[0] %p %d\n", &(a[0]), *(&(a[0])));
	printf("a[1] %p\n", &(a[1]));
	printf("a[2] %p\n", &(a[2]));
	printf("a[3] %p\n", &(a[3]));
	printf("a[4] %p\n", &(a[4]));

	int b[3][3] = { {1, 2, 3,},{4, 5, 6},{7, 8, 9} };
	
	for (int i = 0; i <= 2; i++) {
		for (int j = 0; j <= 2; j++) {
			printf("b[%d][%d] %p %d\n", i, j, &(b[i][j]), b[i][j]);		
		}
	}

	return 0;
}