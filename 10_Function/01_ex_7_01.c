#include <stdio.h>
int main()
{
	void print_star();			//����print_star����
	void print_message();		//����print_message����
	print_star();				//����print_star����
	print_message();			//print_message����
	print_star();				//����print_star����
	return 0;
}

void print_star()				//����print_star����
{
	printf("******************\n");	//���һ��*��
}

void print_message()			//����print_message����
{
	printf("How do you do!\n");	//���һ��������Ϣ
}
