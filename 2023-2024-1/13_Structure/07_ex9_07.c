#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#define N 3			//ѧ����Ϊ3
struct Student			//�����ṹ������struct Student
{
	int num;			//ѧ��
	char name[20];	//����
	float score[3];		//3�ſγɼ�
	float aver;		//ƽ���ɼ�
};
int main()
{
	void input(struct Student stu[]);	//��������
	struct Student max(struct Student stu[]);	//��������
	void print(struct Student stu);	//��������
	struct Student stu[N], * p = stu;	//����ṹ�������ָ��
	input(p);						//����input����
	print(max(p));	//����print����,��max�����ķ���ֵ��Ϊʵ��
	return 0;
}
void input(struct Student stu[])		//����input����
{
	int i;
	printf("�������ѧ������Ϣ�� ѧ�š����������ſγɼ�:\n");
	for (i = 0; i < N; i++)
	{
		scanf("%d %s %f %f %f", &stu[i].num, stu[i].name,
			&stu[i].score[0], &stu[i].score[1], &stu[i].score[2]);	 //��������
		stu[i].aver = (stu[i].score[0] + stu[i].score[1] + stu[i].score[2]) / 3.0;			//��ƽ���ɼ�
	}
}
struct Student max(struct Student stu[])	//����max����
{
	int i, m = 0;			//��m��ųɼ���ߵ�ѧ���������е����
	for (i = 0; i < N; i++)
		if (stu[i].aver > stu[m].aver) m = i;
	//�ҳ�ƽ���ɼ���ߵ�ѧ���������е����
	return stu[m];		//���ذ���������Ϣ�Ľṹ��Ԫ��
}

void print(struct Student stud) 		//����print����
{
	printf("\n�ɼ���ߵ�ѧ����:\n");
	printf("ѧ��:%d\n����:%s\n���ſγɼ�:%5.1f,%5.1f,%5.1f\nƽ���ɼ�: %6.2f\n", stud.num, stud.name, stud.score[0], stud.score[1], stud.score[2], stud.aver);
}
