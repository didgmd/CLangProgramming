<!-- question-meta
id: QB-PG-015
category: 编程题
chapters: 7
concepts: 递归、斐波那契
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 递归斐波那契数列

## 题目




使用递归函数依次求出并输出斐波那契数列从第0项开始的前20项。

### 输入格式

无输入。

### 输出格式

一行输出20个整数，相邻整数以一个空格分隔。

### 数据范围与边界

固定计算 `fib(0)` 至 `fib(19)`，其中 `fib(0)=0`、`fib(1)=1`。

### 样例输入

```text
（无输入）
```

### 样例输出

```text
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
```

## 常见失分点



围绕“递归斐波那契数列”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 明确递归函数的两个终止条件，再逐项调用。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 核对前两项 `0 1`、递推项和第20项 `4181`。

### 完整参考程序

<!-- reference-c:start -->
```c
#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
static long long fib(int n)
{
    return n < 2 ? n : fib(n - 1) + fib(n - 2);
}
int main(void)
{
    for (int i = 0; i < 20; i++)
    {
        printf("%lld%c", fib(i), i == 19 ? '\n' : ' ');
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
