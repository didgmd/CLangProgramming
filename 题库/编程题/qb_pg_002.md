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



围绕“十个数中的最大值”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 用第一个数初始化最大值，再比较其余元素。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 递增数据；全为负数的数据。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    double a [10];
    for(int i = 0; i < 10; i++) if(scanf("%lf", & a [i]) != 1) return 1;
    double m = a [0];
    for(int i = 1; i < 10; i++) if(a [i] > m) m = a [i];
    printf("%.6f\n", m);
    return 0;
}
```
<!-- reference-c:end -->

</details>
