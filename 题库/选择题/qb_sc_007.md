<!-- question-meta
id: QB-SC-007
category: 选择题
chapters: 3
concepts: 算术运算、类型转换
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 整型除法

## 题目

若 `int a=8,b=5; float c;`，执行 `c=a/b+0.4f;` 后 `c` 的值是（ ）。

A. 1.4

B. 1.0

C. 2.0

D. 1.6

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：A。**

`a/b` 先进行整型除法得到 1，再与 0.4 相加。

</details>
