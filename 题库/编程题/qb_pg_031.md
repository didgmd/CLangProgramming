<!-- question-meta
id: QB-PG-031
category: 编程题
chapters: 9
concepts: 结构体、结构体数组、选择排序、结构体整体赋值
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



- 每一趟开始时都要将最高成绩下标初始化为当前起始位置；
- 内层循环从当前起始位置的后一条记录开始；
- 降序排列应选择剩余记录中的最高成绩；
- 一趟查找结束后再交换记录，不能在查找过程中反复交换；
- 交换时必须移动完整结构体，不能只交换成绩；
- 5条记录只需执行4趟选择。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 每轮在尚未确定的记录中寻找最高成绩的下标，再把完整记录交换到当前起始位置。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 使用已降序、已升序和含相同成绩的数据检查下标更新、降序方向和完整记录交换。题目没有规定相同成绩记录的先后顺序。

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
    struct Student students[5];
    struct Student temp;
    int i, j, k;

    for (i = 0; i < 5; i++)
    {
        if (scanf("%d %lf", &students[i].id, &students[i].score) != 2)
        {
            return 1;
        }
    }

    for (i = 0; i < 4; i++)
    {
        k = i;

        for (j = i + 1; j < 5; j++)
        {
            if (students[j].score > students[k].score)
            {
                k = j;
            }
        }

        temp = students[i];
        students[i] = students[k];
        students[k] = temp;
    }

    for (i = 0; i < 5; i++)
    {
        printf("%d %.1f\n", students[i].id, students[i].score);
    }

    return 0;
}
```
<!-- reference-c:end -->

</details>
