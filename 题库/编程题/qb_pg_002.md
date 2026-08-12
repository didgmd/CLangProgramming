<!-- question-meta
id: QB-PG-002
category: 编程题
chapters: 6
concepts: 数组、最大值
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 十个数中的最大值

## 题目



输入10个数，输出最大值。

### 输入格式

10个实数。

### 输出格式

输出最大值，保留6位小数。

### 数据范围与边界

输入恰含10个实数。

### 样例输入

```text
1 2 3 4 5 6 7 8 9 10
```

### 样例输出

```text
10.000000
```

## 常见失分点



使用数组下标 `0` 至 `9` 保存十个数；最大值应由 `a[0]` 初始化，再从 `a[1]` 开始比较。若把最大值初始化为 `0`，全为负数时会得到错误结果；输出必须保留6位小数。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 用第一个数初始化最大值，再比较其余元素。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 递增数据；全为负数的数据；最大值位于首项或重复出现的数据。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>

int main(void)
{
    double a[10];
    double m;

    for (int i = 0; i < 10; i++)
    {
        if (scanf("%lf", &a[i]) != 1)
        {
            return 1;
        }
    }
    m = a[0];

    for (int i = 1; i < 10; i++)
    {
        if (a[i] > m)
        {
            m = a[i];
        }
    }
    printf("%.6f\n", m);
    return 0;
}
```
<!-- reference-c:end -->

</details>
