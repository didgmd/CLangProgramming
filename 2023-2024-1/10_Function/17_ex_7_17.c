#include <stdio.h>
int main()
{
	int fac(int n);
	int i;
	for (i = 1; i <= 5; i++)	//�Ⱥ�5�ε���fac����
		printf("%d!=%d\n", i, fac(i));	//ÿ�μ��㲢���i!��ֵ
	return 0;
}
int fac(int n)
{
	static int f = 1;		//f�������ϴε��ý���ʱ��ֵ
	f = f * n;			//���ϴε�fֵ�Ļ������ٳ���n
	return(f);			//����ֵf��n!��ֵ
}
