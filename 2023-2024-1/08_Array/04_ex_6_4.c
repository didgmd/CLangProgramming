#include <stdio.h>
int main()
{
	int a[2][3] = { {1,2,3},{4,5,6} };
	int b[3][2], i, j;
	printf("array a:\n");
	for (i = 0; i <= 1; i++)			//����a�����е�һ���и�Ԫ��
	{
		for (j = 0; j <= 2; j++)		//����a������ĳһ���и�Ԫ��
		{
			printf("%5d", a[i][j]);	//���a�����һ��Ԫ��
			b[j][i] = a[i][j];	//��a����Ԫ�ص�ֵ����b������ӦԪ��
		}
		printf("\n");
	}
	printf("array b:\n");				//���b�����Ԫ��
	for (i = 0; i <= 2; i++)				//����b������һ���и�Ԫ��
	{
		for (j = 0; j <= 1; j++)			//����b������һ���и�Ԫ��
			printf("%5d", b[i][j]);		//���b�����һ��Ԫ��
		printf("\n");
	}
	return 0;
}
