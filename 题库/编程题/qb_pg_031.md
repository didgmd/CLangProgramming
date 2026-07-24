<!-- question-meta
id: QB-PG-031
category: 编程题
chapters: 9
concepts: 结构体、选择排序
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 结构体选择排序

## 题目




输入5名学生的学号和成绩，使用选择排序按成绩降序排列。

### 输入格式

输入5组记录，每组包含一个整数型学号和一个实数成绩。

### 输出格式

按成绩从高到低输出5行，每行为 `学号 成绩`，成绩保留1位小数。

### 数据范围与边界

固定处理5条记录；交换时必须移动完整结构体。

### 样例输入

```text
1 82
2 75
3 90
4 68
5 88
```

### 样例输出

```text
3 90.0
5 88.0
1 82.0
2 75.0
4 68.0
```

## 常见失分点



围绕“结构体选择排序”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 每轮选择剩余记录中的最低成绩并交换完整记录。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 使用已降序数据和含相同成绩的数据检查完整记录交换。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
struct Student
{
    int id;
    double score;
};
int main(void)
{
    struct Student a[5];
    for (int i = 0; i < 5; i++)
    {
        if (scanf("%d%lf", &a[i].id, &a[i].score) != 2)
        {
            return 1;
        }
    }
    for (int i = 0; i < 4; i++)
    {
        int k = i;
        for (int j = i + 1; j < 5; j++)
        {
            if (a[j].score > a[k].score)
            {
                k = j;
            }
        }
        struct Student t = a[i];
        a[i] = a[k];
        a[k] = t;
    }
    for (int i = 0; i < 5; i++)
    {
        printf("%d %.1f\n", a[i].id, a[i].score);
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
