<!-- question-meta
id: QB-PG-001
category: 编程题
chapters: 4
concepts: 分支、浮点运算
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 一元二次方程

## 题目



输入三个实数系数，完整处理退化、重根、两个实根和复根。

### 输入格式

三个实数 `a b c`。

### 输出格式

按判别式输出实根、重根或共轭复根；退化时输出线性方程结果。

### 数据范围与边界

`|a|<1e-12` 视为退化；浮点结果保留6位小数。

### 样例输入

```text
1 2 1
```

### 样例输出

```text
-1.000000
```

## 常见失分点



围绕“一元二次方程”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 先处理 `a=0` 的退化情形，再按判别式分支。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `1 2 1`（重根）；`0 2 -4`（一次方程）。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <math.h>
#include <stdio.h>
int main(void)
{
    double a, b, c;
    if (scanf("%lf%lf%lf", &a, &b, &c) != 3)
    {
        return 1;
    }
    if (fabs(a) < 1e-12)
    {
        if (fabs(b) < 1e-12)
        {
            puts(fabs(c) < 1e-12 ? "any" : "none");
        }
        else
        {
            printf("%.6f\n", -c / b);
        }
        return 0;
    }
    double d = b * b - 4 * a * c;
    if (d > 1e-12)
    {
        printf("%.6f %.6f\n", (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a));
    }
    else if (fabs(d) <= 1e-12)
    {
        printf("%.6f\n", -b / (2 * a));
    }
    else
    {
        printf(
            "%.6f+%.6fi %.6f-%.6fi\n",
            -b / (2 * a),
            sqrt(-d) / fabs(2 * a),
            -b / (2 * a),
            sqrt(-d) / fabs(2 * a)
        );
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
