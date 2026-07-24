<!-- question-meta
id: QB-SC-064
category: 选择题
chapters: 8
concepts: 指针参数、按值传递
difficulty: 常规
minutes: 3
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 错误的指针交换

## 题目

函数 `void swap(int *a,int *b){int *t=a;a=b;b=t;}` 调用后未交换两个整数，原因是（ ）。

A. 指针不能作参数

B. 只交换了形参指针副本

C. 需要使用数组

D. 整数不能交换

## 常见失分点



本题考查“错误的指针交换”（指针参数、按值传递）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

按值传递使 `a`、`b` 只是调用者地址的副本；应交换 `*a` 与 `*b`。

</details>
