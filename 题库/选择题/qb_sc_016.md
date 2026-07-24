<!-- question-meta
id: QB-SC-016
category: 选择题
chapters: 6
concepts: 字符串结束符
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符串结束符位置

## 题目

执行 `char str[81]="abcdef";` 后，字符串结束符位于（ ）。

A. str[5]

B. str[6]

C. str[7]

D. str[80]

## 常见失分点



本题考查“字符串结束符位置”（字符串结束符）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

6 个可见字符占下标 0～5，`\0` 位于下标 6。

</details>
