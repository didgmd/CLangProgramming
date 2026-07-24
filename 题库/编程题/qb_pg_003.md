<!-- question-meta
id: QB-PG-003
category: 编程题
chapters: 4
concepts: 条件、闰年
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 判断闰年

## 题目



输入年份，判断是否为闰年。

### 输入格式

一个整数年份。

### 输出格式

闰年输出 `leap`，否则输出 `common`。

### 数据范围与边界

按公历闰年规则判断。

### 样例输入

```text
2000
```

### 样例输出

```text
leap
```

## 常见失分点



围绕“判断闰年”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 能被400整除，或能被4整除但不能被100整除。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `2000`（世纪闰年）；`1900`（世纪平年）。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int y;
    if (scanf("%d", &y) != 1)
    {
        return 1;
    }
    puts(y % 400 == 0 || (y % 4 == 0 && y % 100 != 0) ? "leap" : "common");
    return 0;
}
```
<!-- reference-c:end -->

</details>
