<!-- question-meta
id: QB-SC-021
category: 选择题
chapters: 8
concepts: 字符指针、指针运算
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 指针偏移取字符

## 题目

执行 `char str[]="Hello"; char *p=str;` 后，`*(p+4)` 是（ ）。

A. 字符 o

B. '\0'

C. 不确定值

D. 字符 o 的地址

## 常见失分点



本题考查“指针偏移取字符”（字符指针、指针运算）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：A。**

下标 4 对应字符串中的最后一个可见字符 `o`。

</details>
