<!-- question-meta
id: QB-PG-013
category: 编程题
chapters: 6、7
concepts: 冒泡排序、函数
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 浮点数组子函数排序

## 题目



输入10个浮点数，调用排序子函数按升序输出。

### 输入格式

10个实数。

### 输出格式

升序输出排序后的实数。

### 数据范围与边界

输入恰含10个实数。

### 样例输入

```text
3 1 2 4 5 6 7 8 9 0
```

### 样例输出

```text
0.00 1.00 2.00 3.00 4.00 5.00 6.00 7.00 8.00 9.00
```

## 常见失分点



围绕“浮点数组子函数排序”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 在子函数中完成数组排序，主函数负责输入输出。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 逆序数据；含相等元素的数据。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
static void sort(double a [], int n)
{
    for(int j = 0; j < n - 1; j++) for(int i = 0; i < n - 1 - j; i++) if(a [i] > a [i + 1])
    {
        double t = a [i];
        a [i] = a [i + 1];
        a [i + 1] = t;
    }
}
int main(void)
{
    double a [10];
    for(int i = 0; i < 10; i++) if(scanf("%lf", & a [i]) != 1) return 1;
    sort(a, 10);
    for(int i = 0; i < 10; i++) printf("%.2f%c", a [i], i == 9 ? '\n' : ' ');
    return 0;
}
```
<!-- reference-c:end -->

</details>
