#include <stdio.h>

int main() {

	int a = 10;
	int* p = &a;
	printf("八进制   Octonary    (OCT) 0o%o\n", *p);
	printf("八进制   Octonary    (OCT) 0o%16o\n", *p);
	printf("八进制   Octonary    (OCT) 0o%016o\n", *p);
	printf("十六进制 Hexadecimal (HEX) 0x%x\n", *p);
	printf("十六进制 Hexadecimal (HEX) 0x%16x\n", *p);
	printf("十六进制 Hexadecimal (HEX) 0x%016x\n", *p);
	printf("指针形式 Pointer           0p%p\n", *p);

	return 0;
}