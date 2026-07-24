<!-- question-meta
id: QB-PG-010
category: 编程题
chapters: 6
concepts: 二维数组、最大值
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 矩阵最大元素及位置

## 题目



输入3行4列整数矩阵，输出最大元素及其行列下标。

### 输入格式

按行输入3×4整数矩阵。

### 输出格式

输出最大元素及其行、列下标。

### 数据范围与边界

恰输入12个整数；行列下标从0开始。

### 样例输入

```text
1 2 3 4 5 6 20 8 9 10 11 12
```

### 样例输出

```text
20 1 2
```

## 常见失分点



围绕“矩阵最大元素及位置”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 用首元素初始化最大值与位置，再遍历全部元素。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 最大值在中间；所有元素相等。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int a[3][4];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (scanf("%d", &a[i][j]) != 1)
            {
                return 1;
            }
        }
    }
    int r = 0, c = 0;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (a[i][j] > a[r][c])
            {
                r = i;
                c = j;
            }
        }
    }
    printf("%d %d %d\n", a[r][c], r, c);
    return 0;
}
```
<!-- reference-c:end -->

</details>
