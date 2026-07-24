<!-- question-meta
id: QB-PG-035
category: 编程题
chapters: 6
concepts: 字符分类
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 一行字符分类统计

## 题目



统计字母、数字、空格和其他字符，忽略结尾换行。

### 输入格式

一行字符，允许包含空格。

### 输出格式

依次输出英文字母、数字、空格和其他字符的数量。

### 数据范围与边界

读到换行或文件结束为止。

### 样例输入

```text
Ab 3!
```

### 样例输出

```text
2 1 1 1
```

## 常见失分点



围绕“一行字符分类统计”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 按互斥条件依次分类，确保每个字符只计入一类。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 空行；同时含四类字符的一行。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    char s [256];
    if(! fgets(s, sizeof s, stdin)) return 1;
    int a = 0, d = 0, sp = 0, o = 0;
    for(int i = 0; s [i] && s [i] != '\n'; i++)
    {
        if((s [i] >= 'a' && s [i] <= 'z') || (s [i] >= 'A' && s [i] <= 'Z')) a++;
        else if(s [i] >= '0' && s [i] <= '9') d++;
        else if(s [i] == ' ') sp++;
        else o++;
    }
    printf("%d %d %d %d\n", a, d, sp, o);
    return 0;
}
```
<!-- reference-c:end -->

</details>
