#include <stdio.h>

// ����һ���ṹ������ Student
struct Student {
    char name[50];  // ѧ������
    int age;        // ѧ������
    float score;    // ѧ���ɼ�
};

int main() {
    // ����һ�� Student �ṹ���������ʼ��
    struct Student student1;
    strcpy(student1.name, "Alice");
    student1.age = 20;
    student1.score = 85.5;

    // ��ӡѧ����Ϣ
    printf("ѧ������: %s\n", student1.name);
    printf("ѧ������: %d\n", student1.age);
    printf("ѧ���ɼ�: %.2f\n", student1.score);

    return 0;
}
