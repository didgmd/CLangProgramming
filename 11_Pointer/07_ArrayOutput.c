#include <stdio.h>

int main() {

	int a[3] = { 1, 2, 3 };
	// ��������������ʱ��������Ϊ��ַ��ָ�룩
	printf("       a = %p\n",   a);			// &a[0]
	printf("      *a = %d\n",  *a);			//  a[0]
	printf(" (a + 1) = %p\n",  (a + 1));	// &a[1]
	printf("*(a + 1) = %d\n", *(a + 1));	//  a[1]
	printf(" (a + 2) = %p\n",  (a + 2));	// &a[2]
	printf("*(a + 2) = %d\n", *(a + 2));	//  a[2]

	return 0;
}