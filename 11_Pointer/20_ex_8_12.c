#include <stdio.h>
int main()
{
	int a[3][4] = { 1,3,5,7,9,11,13,15,17,19,21,23 };
	int* p;							//p��int *��ָ�����
	for (p = a[0]; p < a[0] + 12; p++)			//ʹp����ָ����һ��Ԫ��
	{
		if ((p - a[0]) % 4 == 0) printf("\n");	//p�ƶ�4�κ���
		printf("%4d", *p);				//���pָ���Ԫ�ص�ֵ 
	}
	printf("\n");
	return 0;
}
