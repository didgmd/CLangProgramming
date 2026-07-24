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

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

6 个可见字符占下标 0～5，`\0` 位于下标 6。

</details>
