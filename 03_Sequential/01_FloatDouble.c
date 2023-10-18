#include <stdio.h>

int main()
{
	double a = 2e-3;
	double b = 2e3;
	double c = 2e+3;
	float f = 3.5;

	printf("a = %lf, b = %lf, c = %lf, f = %f\n", a, b, c, f);

	double d = 3.1415926535897932384;
	float e = 3.1415926535897932384;

	printf("d = %lf, e = %f\n", d, e);

	return 0;
}