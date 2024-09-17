#include <stdio.h>

int main() {

	int a[3] = { 1, 2, 3 };
	// 数组名不加索引时，本质上为地址（指针）
	printf("       a = %p\n",   a);			// &a[0]
	printf("      *a = %d\n",  *a);			//  a[0]
	printf(" (a + 1) = %p\n",  (a + 1));	// &a[1]
	printf("*(a + 1) = %d\n", *(a + 1));	//  a[1]
	printf(" (a + 2) = %p\n",  (a + 2));	// &a[2]
	printf("*(a + 2) = %d\n", *(a + 2));	//  a[2]

	return 0;
}