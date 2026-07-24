<!-- question-meta
id: QB-PG-026
category: 编程题
chapters: 6
concepts: 字符串、溢出
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 带校验的字符串转整数

## 题目



转换带可选符号的十进制字符串，并识别非法输入及溢出。

### 输入格式

一个可带正负号的字符串。

### 输出格式

合法且未溢出时输出对应整数；含非法字符时输出 `invalid`；超出 `int` 范围时输出 `overflow`。

### 数据范围与边界

除首字符的正负号外只能含十进制数字。

### 样例输入

```text
-2048
```

### 样例输出

```text
-2048
```

## 常见失分点



围绕“带校验的字符串转整数”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 单独处理符号，再逐位执行 `value=value*10+digit`。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `-2048`（正常负数）、`12x`（非法字符）、`2147483648`（正溢出）。

### 完整参考程序

<!-- reference-c:start -->
```c
#define __USE_MINGW_ANSI_STDIO 1
#include <limits.h>
#include <stdio.h>
int main(void)
{
    char s[64];
    if (scanf("%63s", s) != 1)
    {
        return 1;
    }
    int i = 0, sign = 1;
    if (s[i] == '+' || s[i] == '-')
    {
        sign = s[i++] == '-' ? -1 : 1;
    }
    if (!s[i])
    {
        puts("invalid");
        return 0;
    }
    long long n = 0;
    for (; s[i]; i++)
    {
        if (s[i] < '0' || s[i] > '9')
        {
            puts("invalid");
            return 0;
        }
        n = n * 10 + s[i] - '0';
        if ((sign == 1 && n > INT_MAX) || (sign == -1 && - n < INT_MIN))
        {
            puts("overflow");
            return 0;
        }
    }
    printf("%lld\n", sign * n);
    return 0;
}
```
<!-- reference-c:end -->

</details>
