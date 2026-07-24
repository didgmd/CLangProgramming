<!-- question-meta
id: QB-SC-050
category: 选择题
chapters: 10
concepts: 文件指针
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 文件指针数量

## 题目

关于文件指针，正确的是（ ）。

A. 一个程序只能有一个

B. 可以定义多个

C. 不能作为参数

D. 只能读文件

## 常见失分点



本题考查“文件指针数量”（文件指针）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

程序可同时定义和使用多个 `FILE *`，分别管理不同文件。

</details>
