#include <stdio.h>
struct Student						//�����ṹ������struct Student
{
	int num;
	float score;
	struct Student* next;
};
int main()
{
	struct Student a, b, c, * head, * p;	//����3���ṹ�����a,b,c��Ϊ�����Ľ��
	a.num = 10101; a.score = 89.5;		//�Խ��a��num��score��Ա��ֵ
	b.num = 10103; b.score = 90;		//�Խ��b��num��score��Ա��ֵ
	c.num = 10107; c.score = 85;		//�Խ��c��num��score��Ա��ֵ
	head = &a;					//�����a����ʼ��ַ����ͷָ��head
	a.next = &b;					//�����b����ʼ��ַ����a����next��Ա
	b.next = &c;					//�����c����ʼ��ַ����a����next��Ա
	c.next = NULL;					//c����next��Ա�������������ַ
	p = head;						//ʹpָ��a���
	do
	{
		printf("%ld %5.1f\n", p->num, p->score);	//���pָ��Ľ�������
		p = p->next;				//ʹpָ����һ���
	} while (p != NULL);				//�����c����p��ֵΪNULL��ѭ����ֹ
	return 0;
}