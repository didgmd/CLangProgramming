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

- 行下标范围是0至2，列下标范围是0至3，不能混淆两个循环边界。
- 最大值应由真实元素 `a[0][0]` 初始化，不能初始化为0，否则全负矩阵会出错。
- 发现更大元素时，必须同时更新最大值、行下标和列下标。
- 多个元素同为最大值时，使用严格大于号可以保留第一次出现的位置。
- 输出顺序是“最大元素、行下标、列下标”。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 用首元素初始化最大值与位置，再遍历全部元素。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 最大值在中间；所有元素相等；所有元素均为负数。

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
    int maximum = a[0][0];
    int row = 0;
    int column = 0;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (a[i][j] > maximum)
            {
                maximum = a[i][j];
                row = i;
                column = j;
            }
        }
    }

    printf("%d %d %d\n", maximum, row, column);
    return 0;
}
```
<!-- reference-c:end -->

</details>
