#include <stdio.h>
int main()
{
	int f(int);				//��������
	int a = 2, i;				//�Զ��ֲ�����
	for (i = 0; i < 3; i++)
		printf("%d\n", f(a));	//���f(a)��ֵ
	return 0;
}

int f(int a)
{
	auto int b = 0;			//�Զ��ֲ�����
	static int c = 3;			//��̬�ֲ�����
	b = b + 1;
	c = c + 1;
	return(a + b + c);
}
