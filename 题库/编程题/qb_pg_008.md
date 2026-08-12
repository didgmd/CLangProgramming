<!-- question-meta
id: QB-PG-008
category: 编程题
chapters: 6
concepts: 选择排序
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 选择法排序

## 题目



输入10个整数，使用选择法升序输出。

### 输入格式

10个整数，以空白分隔。

### 输出格式

一行输出升序排列后的10个整数。

### 数据范围与边界

输入恰含10个 `int` 范围内的整数。

### 样例输入

```text
10 9 8 7 6 5 4 3 2 1
```

### 样例输出

```text
1 2 3 4 5 6 7 8 9 10
```

## 常见失分点

- 每一趟开始时都要执行 `k = i`，把当前位置作为最小值位置的初值。
- 内层循环应从 `i + 1` 开始，只检查尚未排序的部分。
- 比较过程中只更新最小元素下标 `k`，一趟查找结束后再交换。
- 交换时必须使用临时变量，避免原值被覆盖。
- 输出相邻整数之间只有一个空格，行末输出换行。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 第 `i` 趟在下标 `i` 至 `9` 中找出最小元素的下标 `k`，再交换 `a[i]` 与 `a[k]`。完成9趟后，10个整数按升序排列。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 逆序数据；已有序数据；含负数和重复值的数据。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int a[10];
    for (int i = 0; i < 10; i++)
    {
        if (scanf("%d", &a[i]) != 1)
        {
            return 1;
        }
    }
    for (int i = 0; i < 9; i++)
    {
        int k = i;
        for (int j = i + 1; j < 10; j++)
        {
            if (a[j] < a[k])
            {
                k = j;
            }
        }
        int t = a[i];
        a[i] = a[k];
        a[k] = t;
    }
    for (int i = 0; i < 10; i++)
    {
        if (i > 0)
        {
            printf(" ");
        }

        printf("%d", a[i]);
    }

    printf("\n");
    return 0;
}
```
<!-- reference-c:end -->

</details>
