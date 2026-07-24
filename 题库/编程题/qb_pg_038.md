<!-- question-meta
id: QB-PG-038
category: 编程题
chapters: 8
concepts: 字符指针、指针差
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 指针法求字符串长度

## 题目



不调用 `strlen`，使用两个指针之差求字符串长度。

### 输入格式

一行长度不超过99的字符串。

### 输出格式

输出字符串长度。

### 数据范围与边界

长度不包含末尾 `\0`，允许输入空行。

### 样例输入

```text
hello world
```

### 样例输出

```text
11
```

## 常见失分点



围绕“指针法求字符串长度”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 用指针从首字符移动到 `\0`，指针差即长度。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `hello world`；空行。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
static int length(const char * s)
{
    const char * p = s;
    while (* p)
    {
        p++;
    }
    return(int) (p - s);
}
int main(void)
{
    char s[128];
    if (!fgets(s, sizeof s, stdin))
    {
        return 1;
    }
    int n = length(s);
    if (n > 0 && s[n - 1] == '\n')
    {
        n--;
    }
    printf("%d\n", n);
    return 0;
}
```
<!-- reference-c:end -->

</details>
