<!-- question-meta
id: QB-PG-028
category: 编程题
chapters: 7
concepts: 递归、数组
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 递归生成斐波那契数组

## 题目



用递归函数生成并输出前20项。

### 输入格式

一个整数 `n`。

### 输出格式

输出斐波那契数列的前 `n` 项。

### 数据范围与边界

使用参考程序可安全表示的正整数范围。

### 样例输入

```text
6
```

### 样例输出

```text
1 1 2 3 5 8
```

## 常见失分点



围绕“递归生成斐波那契数组”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 明确递归函数的两个终止条件，再逐项调用。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `n=1`（最小规模）；`n=6`（一般情况）。

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
    for(int i = 0; i < 20; i++) printf("%lld%c", fib(i), i == 19 ? '\n' : ' ');
    return 0;
}
```
<!-- reference-c:end -->

</details>
