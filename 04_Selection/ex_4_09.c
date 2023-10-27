#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
#include <math.h>
int main()
{
	double a, b, c, disc, x1, x2, realpart, imagpart;
	scanf("%lf,%lf,%lf", &a, &b, &c);
	printf("The equation ");
	if (fabs(a) <= 1e-6)
		printf("is not a quadratic\n");
	else
	{
		disc = b * b - 4 * a * c;
		if (fabs(disc) <= 1e-6)
			printf("has two equal roots:%8.4f\n", -b / (2 * a));
		else
			if (disc > 1e-6)
			{
				x1 = (-b + sqrt(disc)) / (2 * a);
				x2 = (-b - sqrt(disc)) / (2 * a);
				printf("has distinct real roots:%8.4f and %8.4f\n", x1, x2);
			}
			else
			{
				realpart = -b / (2 * a);			//realpart�Ǹ�����ʵ��
				imagpart = sqrt(-disc) / (2 * a);	//imagpart�Ǹ������鲿
				printf("has complex roots:\n");
				printf("%8.4f+%8.4fi\n", realpart, imagpart);	//���һ������
				printf("%8.4f-%8.4fi\n", realpart, imagpart);	//�����һ������
			}
	}
	return 0;
}
