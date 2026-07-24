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



输入10个景点距离，用选择法同步排序距离和原编号。

### 输入格式

若干组景点编号与距离。

### 输出格式

按距离升序同步输出编号和距离。

### 数据范围与边界

编号与距离必须作为同一记录同步交换。

### 样例输入

```text
3
101 8.5
102 3.0
103 5.5
```

### 样例输出

```text
102 3.00
103 5.50
101 8.50
```

## 常见失分点



围绕“景点距离与编号同步排序”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 比较距离时同时交换对应编号，保持记录关联。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 距离逆序；含相同距离。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int d [10], id [10];
    for(int i = 0; i < 10; i++)
    {
        if(scanf("%d", & d [i]) != 1) return 1;
        id [i] = i;
    }
    for(int i = 0; i < 9; i++)
    {
        int k = i;
        for(int j = i + 1; j < 10; j++) if(d [j] < d [k]) k = j;
        int td = d [i];
        d [i] = d [k];
        d [k] = td;
        int ti = id [i];
        id [i] = id [k];
        id [k] = ti;
    }
    for(int i = 0; i < 10; i++) printf("%d:%d%c", id [i], d [i], i == 9 ? '\n' : ' ');
    return 0;
}
```
<!-- reference-c:end -->

</details>
