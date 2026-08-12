<!-- question-meta
id: QB-PG-017
category: 编程题
chapters: 7、8
concepts: 字符串复制、指针
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 不用字符串库复制

## 题目



输入一个不含空白字符的字符串，调用自定义函数复制并输出。

### 输入格式

一个长度不超过79且不含空白字符的字符串。

### 输出格式

输出复制后的字符串。

### 数据范围与边界

输入字符串不含空白字符，长度不超过79，并为目标数组末尾的 `\0` 留出位置。

### 样例输入

```text
C_language
```

### 样例输出

```text
C_language
```

## 常见失分点



注意源字符串与目标字符串的方向、两个指针的同步移动、末尾 `\0` 的补写、目标数组容量和形参顺序。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 逐字符复制可见字符；源指针和目标指针同步移动，最后显式补写 `\0`。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 普通字符串；单字符；79字符上界。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>

static void copy_string(char * from, char * to)
{
    while (* from != '\0')
    {
        * to = * from;
        from++;
        to++;
    }

    * to = '\0';
}

int main(void)
{
    char source[80];
    char destination[80];

    if (scanf("%79s", source) != 1)
    {
        return 1;
    }

    copy_string(source, destination);
    printf("%s\n", destination);

    return 0;
}
```
<!-- reference-c:end -->

</details>
