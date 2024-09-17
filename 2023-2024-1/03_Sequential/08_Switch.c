#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main()
{
	int a;

	printf("请问你想去几层？\n");

	scanf("%d", &a);

	switch (a)
	{
		case 1:
			printf("去第一层\n");
			break;
		case 2:
			printf("去第二层\n");
			break;
		case 3:
			printf("去第三层\n");
			break;
		case 4:
			printf("去第四层\n");
			break;
		default:
			printf("没有这个楼层\n");
			break;
	}

	return 0;
}