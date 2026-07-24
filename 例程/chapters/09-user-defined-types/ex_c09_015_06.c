/*
 * 例程 ID：EX-C09-015
 * 标题：实验演示 lab5.6
 * 教材位置：第 9 章 / lab5.6
 * 知识点：结构体、枚举、链表、自定义数据类型
 * 来源：2023-2024-1/14_Lab5/06.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：可移植例程：按 C11 子集验证。
 */
#include <stdio.h>

enum DayOfWeek {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday
};

int main() {
    enum DayOfWeek today = Wednesday;
    switch (today) {
		case Monday:
			printf("Today is Monday\n");
			break;
		case Tuesday:
			printf("Today is Tuesday\n");
			break;
		case Wednesday:
			printf("Today is Wednesday\n");
			break;
		case Thursday:
			printf("Today is Thursday\n");
			break;
		case Friday:
			printf("Today is Friday\n");
			break;
		case Saturday:
			printf("Today is Saturday\n");
			break;
		case Sunday:
			printf("Today is Sunday\n");
			break;
	}

    return 0;
}
