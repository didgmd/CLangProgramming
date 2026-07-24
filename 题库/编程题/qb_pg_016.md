<!-- question-meta
id: QB-PG-016
category: 编程题
chapters: 6
concepts: 选择排序、平行数组
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 景点距离与编号同步排序

## 题目




输入10个景点距离，使用选择排序按距离升序排列，并同步保留各距离原来的下标编号。

### 输入格式

输入10个整数距离，以空白分隔。

### 输出格式

按距离升序输出10组 `原下标:距离`，相邻记录以一个空格分隔。

### 数据范围与边界

下标编号固定为0至9；输入距离应在 `int` 范围内。

### 样例输入

```text
8 3 5 1 9 2 7 4 6 0
```

### 样例输出

```text
9:0 3:1 5:2 1:3 7:4 2:5 8:6 6:7 0:8 4:9
```

## 常见失分点



围绕“景点距离与编号同步排序”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 比较距离时同时交换对应编号，保持记录关联。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 使用逆序距离检查排序，并用重复距离检查编号始终与距离同步。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int d[10], id[10];
    for (int i = 0; i < 10; i++)
    {
        if (scanf("%d", &d[i]) != 1)
        {
            return 1;
        }
        id[i] = i;
    }
    for (int i = 0; i < 9; i++)
    {
        int k = i;
        for (int j = i + 1; j < 10; j++)
        {
            if (d[j] < d[k])
            {
                k = j;
            }
        }
        int td = d[i];
        d[i] = d[k];
        d[k] = td;
        int ti = id[i];
        id[i] = id[k];
        id[k] = ti;
    }
    for (int i = 0; i < 10; i++)
    {
        printf("%d:%d%c", id[i], d[i], i == 9 ? '\n' : ' ');
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
