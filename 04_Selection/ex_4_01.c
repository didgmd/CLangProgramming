#define _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
#include<math.h>		//������Ҫ������ƽ��������sqrt
int main()
{
	double a, b, c, disc, x1, x2, p, q;	//disc���б�ʽsqrt(b*b-4ac)  
	scanf("%lf%lf%lf", &a, &b, &c);	//����˫���ȸ����ͱ�����ֵҪ�ø�ʽ����"%lf"  
	disc = b * b - 4 * a * c;
	if (disc < 0)					//��b*b-4ac<0
		printf("This equation hasn't real roots\n");	//������˷�����ʵ����
	else						//b*b-4ac��0
	{
		p = -b / (2.0 * a);
		q = sqrt(disc) / (2.0 * a);
		x1 = p + q; x2 = p - q;		//������̵�������  
		printf("real roots:\nx1=%7.2f\nx2=%7.2f\n", x1, x2);	//������̵�������  
	}
	return 0;
}