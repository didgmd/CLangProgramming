/*
 * 例程 ID：EX-C06-012
 * 标题：教材例程 custom-10_string
 * 教材位置：第 6 章 / custom-10_string
 * 知识点：一维数组、二维数组、字符数组、字符串
 * 来源：2023-2024-1/08_Array/10_String.c
 * 编译模式：c11-strict
 * 旧语法：无
 * 交互方式：manual
 * 兼容性：教学风险演示：a[5] 不含结尾 '\0'，使用 %s 的输出未定义；仅限手动观察，不用于生产程序。
 */
#include <stdio.h>

/*
 * 教学演示：a 恰好容纳 5 个字符，不包含字符串结尾 '\0'。
 * 下面的 %s 调用故意保留，用于观察未定义输出；不可照搬到生产程序。
 */

int main() {
	char a[5] = "China";
	char b[6] = "China";

	for (int i = 0; i <= 4; i++) {
		printf("%c", a[i]);
	}

	printf("\n");

	printf("a: %s\n", a);
	printf("b: %s\n", b);

	return 0;
}
