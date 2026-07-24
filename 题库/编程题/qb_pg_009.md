<!-- question-meta
id: QB-PG-009
category: 编程题
chapters: 5
concepts: 素数、嵌套循环
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 区间素数

## 题目



输出100到200之间的全部素数，每行5个。

### 输入格式

两个整数 `m n`。

### 输出格式

按升序输出闭区间 `[m,n]` 内的素数，以空格分隔。

### 数据范围与边界

`m<=n`；小于2的整数不是素数。

### 样例输入

```text
10 20
```

### 样例输出

```text
11 13 17 19
```

## 常见失分点



围绕“区间素数”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 逐个检查候选数，试除上界取其平方根。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `10 20`（正常区间）；`0 2`（跨越素数下界）。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int count = 0;
    for(int n = 100; n <= 200; n++)
    {
        int p = 1;
        for(int i = 2; i <= n / i && p; i++) if(n % i == 0) p = 0;
        if(p)
        {
            printf("%d%c", n,++ count % 5 ? ' ' : '\n');
        }
    }
    if(count % 5) putchar('\n');
    return 0;
}
```
<!-- reference-c:end -->

</details>
