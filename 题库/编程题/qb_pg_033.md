<!-- question-meta
id: QB-PG-033
category: 编程题
chapters: 8
concepts: 字符指针、复制
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 指针复制字符串

## 题目



使用字符指针完成字符串复制并保留结束符。

### 输入格式

一个长度受限、可含空格的字符串。

### 输出格式

输出复制后的字符串。

### 数据范围与边界

输入长度必须小于目标数组容量，并为末尾 `\0` 留出位置。

### 样例输入

```text
C language
```

### 样例输出

```text
C language
```

## 常见失分点



围绕“指针复制字符串”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 逐字符复制，并在复制字符 `\0` 后停止。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 空行；普通短字符串。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
static void copy_string(const char * a, char * b)
{
    while((* b++ = * a++) != '\0')
    {
    }
}
int main(void)
{
    char a [80], b [80];
    if(! fgets(a, sizeof a, stdin)) return 1;
    copy_string(a, b);
    printf("%s", b);
    return 0;
}
```
<!-- reference-c:end -->

</details>
