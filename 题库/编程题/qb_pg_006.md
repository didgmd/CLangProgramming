<!-- question-meta
id: QB-PG-006
category: 编程题
chapters: 5
concepts: 素数、试除
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 判断整数是否为素数

## 题目



输入整数，判断是否为素数。

### 输入格式

一个整数 `n`。

### 输出格式

输出 `prime` 或 `not prime`。

### 数据范围与边界

`n<2` 不是素数。

### 样例输入

```text
17
```

### 样例输出

```text
prime
```

## 常见失分点



`n<2`必须判为非素数；试除范围不能遗漏平方根附近的因数；循环变量和素数标志必须正确初始化并更新；输出必须严格使用`prime`或`not prime`。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 从2开始试除。`is_prime`保存当前判断状态；循环在发现因数或试除数超过平方根附近时结束。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `17`；`21`；`2`；`1`；`49`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int n;
    int i = 2;
    int is_prime = 1;

    if (scanf("%d", &n) != 1)
    {
        return 1;
    }

    if (n < 2)
    {
        is_prime = 0;
    }

    while (is_prime && i <= n / i)
    {
        if (n % i == 0)
        {
            is_prime = 0;
        }

        i++;
    }

    if (is_prime)
    {
        printf("prime\n");
    }
    else
    {
        printf("not prime\n");
    }

    return 0;
}
```
<!-- reference-c:end -->

</details>
