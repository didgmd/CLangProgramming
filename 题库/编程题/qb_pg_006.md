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



围绕“判断整数是否为素数”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 试除到 `i*i<=n` 即可。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `2`；`1`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int n;
    if (scanf("%d", &n) != 1)
    {
        return 1;
    }
    int p = n >= 2;
    for (int i = 2; i <= n / i && p; i++)
    {
        if (n % i == 0)
        {
            p = 0;
        }
    }
    puts(p ? "prime" : "not prime");
    return 0;
}
```
<!-- reference-c:end -->

</details>
