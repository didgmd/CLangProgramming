#include <stdio.h>

int main()
{
	char c1, c2;

	c1 = getchar();	//�Ӽ��̶���һ����д��ĸ�������ַ�����c1
	c2 = c1 + 32;	//�õ���Ӧ��Сд��ĸ��ASCII���룬�����ַ�����c2��
	
	printf("��д��ĸ: %c\nСд��ĸ: %c\n", c1, c2);	//���c1,c2��ֵ
	
	return 0;
}
