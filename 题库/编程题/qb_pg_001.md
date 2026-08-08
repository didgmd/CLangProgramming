<!-- question-meta
id: QB-PG-001
category: 编程题
chapters: 4
concepts: 多分支、判别式、浮点运算
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 一元二次方程

## 题目



输入一元二次方程的三个实数系数，分别处理两个实根、重根和共轭复根。

### 输入格式

三个实数 `a b c`。

### 输出格式

按判别式输出两个实根、重根或共轭复根。

### 数据范围与边界

`|a|>=1e-12`，保证方程为一元二次方程；浮点结果保留6位小数。

### 样例输入

```text
1 2 1
```

### 样例输出

```text
-1.000000
```

## 常见失分点



先计算判别式 `d=b*b-4*a*c`，再根据 `d` 为正、接近零或为负选择对应公式。注意两个实根的输出顺序、复根虚部的正负号，以及题目规定的六位小数格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 计算判别式，再按其为正、接近零或为负分别计算两个实根、重根或共轭复根。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `1 -3 2`（两个实根）；`1 2 1`（重根）；`1 2 5`（共轭复根）。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <math.h>
#include <stdio.h>
int main(void)
{
    double a, b, c;
    double d, x1, x2;
    double real_part, imag_part;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3)
    {
        return 1;
    }

    d = b * b - 4.0 * a * c;

    if (d > 1e-12)
    {
        x1 = (-b + sqrt(d)) / (2.0 * a);
        x2 = (-b - sqrt(d)) / (2.0 * a);
        printf("%.6f %.6f\n", x1, x2);
    }
    else if (fabs(d) <= 1e-12)
    {
        printf("%.6f\n", -b / (2.0 * a));
    }
    else
    {
        real_part = -b / (2.0 * a);
        imag_part = sqrt(-d) / fabs(2.0 * a);
        printf(
            "%.6f+%.6fi %.6f-%.6fi\n",
            real_part,
            imag_part,
            real_part,
            imag_part
        );
    }

    return 0;
}
```
<!-- reference-c:end -->

</details>
