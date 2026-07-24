<!-- question-meta
id: QB-PG-011
category: 编程题
chapters: 5
concepts: 循环、数位分解
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 水仙花数

## 题目



输出全部三位水仙花数。

### 输入格式

无输入。

### 输出格式

输出所有三位水仙花数，每个一行。

### 数据范围与边界

三位数范围为100至999。

### 样例输入

```text
（无输入）
```

### 样例输出

```text
153
370
371
407
```

## 常见失分点



围绕“水仙花数”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 分解百、十、个位并比较各位立方和。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 核对153和407均被输出。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    for (int n = 100; n <= 999; n++)
    {
        int a = n / 100, b = n / 10 % 10, c = n % 10;
        if (a * a * a + b * b * b + c * c * c == n)
        {
            printf("%d\n", n);
        }
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
