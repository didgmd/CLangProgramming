<!-- question-meta
id: QB-PG-021
category: 编程题
chapters: 6
concepts: 二维数组、矩阵转置
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 三阶矩阵转置

## 题目



输入3阶矩阵，将转置结果保存到另一矩阵并输出。

### 输入格式

按行输入一个3×3整数矩阵。

### 输出格式

按行输出其转置矩阵，每行元素以空格分隔。

### 数据范围与边界

恰输入9个 `int` 范围内的整数。

### 样例输入

```text
1 2 3 4 5 6 7 8 9
```

### 样例输出

```text
1 4 7
2 5 8
3 6 9
```

## 常见失分点



围绕“三阶矩阵转置”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 输出位置 `(i,j)` 应读取原矩阵位置 `(j,i)`。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 顺序矩阵；对称矩阵。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int a[3][3], b[3][3];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (scanf("%d", &a[i][j]) != 1)
            {
                return 1;
            }
        }
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            b[j][i] = a[i][j];
        }
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d%c", b[i][j], j == 2 ? '\n' : ' ');
        }
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
