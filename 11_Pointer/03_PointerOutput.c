#include <stdio.h>

int main() {

	int a = 10;
	int* p = &a;
	printf("�˽���   Octonary    (OCT) 0o%o\n", *p);
	printf("�˽���   Octonary    (OCT) 0o%16o\n", *p);
	printf("�˽���   Octonary    (OCT) 0o%016o\n", *p);
	printf("ʮ������ Hexadecimal (HEX) 0x%x\n", *p);
	printf("ʮ������ Hexadecimal (HEX) 0x%16x\n", *p);
	printf("ʮ������ Hexadecimal (HEX) 0x%016x\n", *p);
	printf("ָ����ʽ Pointer           0p%p\n", *p);

	return 0;
}