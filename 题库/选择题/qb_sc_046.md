<!-- question-meta
id: QB-SC-046
category: 选择题
chapters: 7
concepts: 递归、跟踪
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 递归函数求值

## 题目

函数 `f(1)=2`，`f(n)=n-f(n-1)`，则 `f(3)` 为（ ）。

A. 1

B. 2

C. 3

D. 4

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

`f(2)=2-2=0`，`f(3)=3-0=3`。

</details>
