<!-- question-meta
id: QB-PG-004
category: 编程题
chapters: 6
concepts: 冒泡排序
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 十个整数冒泡排序

## 题目



输入10个整数，使用冒泡法升序输出。

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



内层循环必须比较相邻的 `a[i]` 与 `a[i + 1]`，并把边界写成 `i < 9 - j`，避免越界且跳过已就位的末尾元素。交换时应保留临时值；输出空格不能多写或漏写。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 按题目指定的排序方法比较并交换，注意内层循环的有效范围。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 逆序数据；已有序数据；含重复值的数据。

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
    for (int j = 0; j < 9; j++)
    {
        for (int i = 0; i < 9 - j; i++)
        {
            if (a[i] > a[i + 1])
            {
                int t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
            }
        }
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
