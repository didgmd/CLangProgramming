#include <stdio.h>
#include <stdlib.h>

struct student
{
    int id;
    char name;
    char sex;
    int age;
    int score;
};	// 注意最后有一个分号

int main()
{
    struct student stu;
    struct student *pStu;

    pStu = (struct student *)malloc(sizeof(struct student));

    printf("%p\n", &stu);
    stu.id = 123;
    stu.name = 'a';
    stu.sex = 'm';
    stu.age = 20;
    stu.score = 95;

    printf("%p\n", pStu);
    pStu->id = 321;
    pStu->name = 'A';
    pStu->sex = 'f';
    pStu->age = 20;
    pStu->score = 96;

    return 0;
}