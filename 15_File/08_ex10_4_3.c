#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#define SIZE 3
struct Student_type
{
	char name[10];
	int num;
	int age;
	char addr[15];
}stud[SIZE];	//����ȫ�ֽṹ������stud������10��ѧ������

void load()
{
	FILE* fp;
	int i;
	if ((fp = fopen("stu.dat", "rb")) == NULL) //�������ļ�stu.dat
	{
		printf("cannot open infile\n");
		return;
	}
	for (i = 0; i < SIZE; i++)
		if (fread(&stud[i], sizeof(struct Student_type), 1, fp) != 1)
			//��stu.dat�ļ��ж�����
		{
			if (feof(fp))	//����ļ���������ر��ļ�������
			{
				fclose(fp);
				return;
			}
			printf("file read error\n");
		}
	fclose(fp);
}

void save()	//���庯��save�����ļ����SIZE��ѧ��������
{
	FILE* fp;
	int i;
	if ((fp = fopen("stu2.dat", "wb")) == NULL)	//������ļ�stu2.dat
	{
		printf("cannot open file\n");
		return;
	}
	for (i = 0; i < SIZE; i++)
		if (fwrite(&stud[i], sizeof(struct Student_type), 1, fp) != 1)
			printf("file write error\n");
	fclose(fp);
}
int main()
{
	int i;
	load();
	save();
	return 0;
}
