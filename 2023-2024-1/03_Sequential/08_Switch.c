#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main()
{
	int a;

	printf("��������ȥ���㣿\n");

	scanf("%d", &a);

	switch (a)
	{
		case 1:
			printf("ȥ��һ��\n");
			break;
		case 2:
			printf("ȥ�ڶ���\n");
			break;
		case 3:
			printf("ȥ������\n");
			break;
		case 4:
			printf("ȥ���Ĳ�\n");
			break;
		default:
			printf("û�����¥��\n");
			break;
	}

	return 0;
}