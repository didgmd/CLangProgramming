#include <stdio.h>
int main()
{
	char a[] = "I am a student.", b[20];	//�����ַ�����
	int i;
	for (i = 0; *(a + i) != '\0'; i++)
		*(b + i) = *(a + i);		//��a[i]��ֵ����b[i]
	*(b + i) = '\0'; 			//��b�������Ч�ַ�֮���'\0'
	printf("string a is:%s\n", a);//���a������ȫ����Ч�ַ�
	printf("string b is:");
	for (i = 0; b[i] != '\0'; i++)
		printf("%c", b[i]);	//������b������ȫ����Ч�ַ�
	printf("\n");
	return 0;
}
