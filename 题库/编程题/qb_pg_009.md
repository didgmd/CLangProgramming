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




输出100到200之间的全部素数，每行最多输出5个。

### 输入格式

无输入。

### 输出格式

按升序输出100到200之间的素数，每行5个，最后一行可以不足5个。

### 数据范围与边界

候选整数固定为闭区间 `[100, 200]`。

### 样例输入

```text
（无输入）
```

### 样例输出

```text
101 103 107 109 113
127 131 137 139 149
151 157 163 167 173
179 181 191 193 197
199
```

## 常见失分点



围绕“区间素数”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 逐个检查候选数，试除上界取其平方根。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 核对首个结果为101、末个结果为199，并检查每行数量。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int count = 0;
    for (int n = 100; n <= 200; n++)
    {
        int p = 1;
        for (int i = 2; i <= n / i && p; i++)
        {
            if (n % i == 0)
            {
                p = 0;
            }
        }
        if (p)
        {
            if (count % 5)
            {
                putchar(' ');
            }
            printf("%d", n);
            count++;
            if (count % 5 == 0)
            {
                putchar('\n');
            }
        }
    }
    if (count % 5)
    {
        putchar('\n');
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
