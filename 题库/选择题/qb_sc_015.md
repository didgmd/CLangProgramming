<!-- question-meta
id: QB-SC-015
category: 选择题
chapters: 6
concepts: 字符数组、字符串结束符
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符串占用字节

## 题目

`char a[]="one\n";` 中数组占用的字节数是（ ）。

A. 3

B. 4

C. 5

D. 6

## 常见失分点



本题考查“字符串占用字节”（字符数组、字符串结束符）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

三个字母、一个换行字符和结尾 `\0` 共 5 字节。

</details>
