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



- 递归出口必须同时正确处理 `0!` 和 `1!`。
- 递归调用必须使参数由 `n` 变为 `n-1`，逐步接近出口。
- `20!` 需要 `long long` 及匹配的 `%lld` 格式。
- 计算前必须拒绝负数和大于20的输入。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 递归终止条件为 `n<=1`，递推步骤为 `n*f(n-1)`。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `0`、`5`、`20`、`-1`和`21`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>

long long factorial(int n);

int main(void)
{
    int n;

    if (scanf("%d", &n) != 1 || n < 0 || n > 20)
    {
        puts("invalid");
        return 0;
    }

    printf("%lld\n", factorial(n));
    return 0;
}

long long factorial(int n)
{
    if (n <= 1)
    {
        return 1;
    }

    return n * factorial(n - 1);
}
```
<!-- reference-c:end -->

</details>
