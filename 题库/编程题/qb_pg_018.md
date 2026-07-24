<!-- question-meta
id: QB-PG-018
category: 编程题
chapters: 7
concepts: 递归、阶乘
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 递归阶乘

## 题目



输入0到20之间的整数，递归计算阶乘；非法输入输出 `invalid`。

### 输入格式

一个非负整数 `n`。

### 输出格式

输出 `n!`。

### 数据范围与边界

输入范围受返回类型限制；负数输入无定义，应拒绝。

### 样例输入

```text
5
```

### 样例输出

```text
120
```

## 常见失分点



围绕“递归阶乘”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 递归终止条件为 `n<=1`，递推步骤为 `n*f(n-1)`。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `0`（边界，结果为1）；`5`（一般情况）。

### 完整参考程序

<!-- reference-c:start -->
```c
#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
static unsigned long long fac(unsigned n)
{
    return n < 2 ? 1 : n * fac(n - 1);
}
int main(void)
{
    int n;
    if(scanf("%d", & n) != 1 || n < 0 || n > 20)
    {
        puts("invalid");
        return 0;
    }
    printf("%llu\n", fac((unsigned) n));
    return 0;
}
```
<!-- reference-c:end -->

</details>
