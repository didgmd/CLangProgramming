#include <stdio.h>
int main()
{
	int i;
	int f[20] = { 1,1 };				//����ǰ������Ԫ��f[0]��f[1]����ֵ1
	for (i = 2; i < 20; i++)
		f[i] = f[i - 2] + f[i - 1];		//�Ⱥ����f[2]~f[19]��ֵ
	for (i = 0; i < 20; i++)
	{
		if (i % 5 == 0) printf("\n"); 	//����ÿ���5��������
		printf("%12d", f[i]);		//���һ����
	}
	printf("\n");
	return 0;
}