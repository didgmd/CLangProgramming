<!-- question-meta
id: QB-PG-027
category: 编程题
chapters: 6
concepts: 字符转换
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 英文字母大小写互换

## 题目



输入一行，把英文字母大小写互换，其他字符保持不变。

### 输入格式

一行字符。

### 输出格式

输出大小写互换后的字符序列。

### 数据范围与边界

仅英文字母改变，其他字符原样保留。

### 样例输入

```text
AbC 12
```

### 样例输出

```text
aBc 12
```

## 常见失分点



围绕“英文字母大小写互换”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 分别判断大写与小写字母，利用字符差值转换。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 大小写混合；含非字母字符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    char s [256];
    if(! fgets(s, sizeof s, stdin)) return 1;
    for(int i = 0; s [i]; i++)
    {
        if(s [i] >= 'a' && s [i] <= 'z') s [i] -= 'a' - 'A';
        else if(s [i] >= 'A' && s [i] <= 'Z') s [i] += 'a' - 'A';
    }
    printf("%s", s);
    return 0;
}
```
<!-- reference-c:end -->

</details>
