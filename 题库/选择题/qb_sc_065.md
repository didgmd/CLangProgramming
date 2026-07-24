<!-- question-meta
id: QB-SC-065
category: 选择题
chapters: 8
concepts: 未初始化指针、未定义行为
difficulty: 常规
minutes: 3
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 未初始化指针诊断

## 题目

执行 `int *p; *p=10;` 的主要问题是（ ）。

A. p 指向常量

B. p 未指向有效对象

C. 10 不能赋给整数

D. 缺少循环

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

未初始化指针保存不确定地址，解引用会产生未定义行为。

</details>
