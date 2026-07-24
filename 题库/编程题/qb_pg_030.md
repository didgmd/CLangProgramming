<!-- question-meta
id: QB-PG-030
category: 编程题
chapters: 9
concepts: 结构体、冒泡排序
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 结构体冒泡排序

## 题目



输入5名学生学号和成绩，按成绩降序冒泡排序。

### 输入格式

若干学生记录，每条含学号、姓名和成绩。

### 输出格式

按成绩升序输出全部记录。

### 数据范围与边界

记录数不得超过数组容量；交换整个结构体。

### 样例输入

```text
3
1 Li 82
2 Wang 75
3 Zhao 90
```

### 样例输出

```text
2 Wang 75
1 Li 82
3 Zhao 90
```

## 常见失分点



围绕“结构体冒泡排序”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 用冒泡排序比较成绩，并同步交换完整记录。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 成绩逆序；含相同成绩。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
struct Student
{
    int id;
    double score;
}
;
int main(void)
{
    struct Student a [5];
    for(int i = 0; i < 5; i++) if(scanf("%d%lf", & a [i].id, & a [i].score) != 2) return 1;
    for(int j = 0; j < 4; j++) for(int i = 0; i < 4 - j; i++) if(a [i].score < a [i + 1].score)
    {
        struct Student t = a [i];
        a [i] = a [i + 1];
        a [i + 1] = t;
    }
    for(int i = 0; i < 5; i++) printf("%d %.1f\n", a [i].id, a [i].score);
    return 0;
}
```
<!-- reference-c:end -->

</details>
