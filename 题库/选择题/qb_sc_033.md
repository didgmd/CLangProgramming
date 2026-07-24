<!-- question-meta
id: QB-SC-033
category: 选择题
chapters: 5
concepts: 空语句、while
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 空语句陷阱

## 题目

`while(--i);` 中分号的作用是（ ）。

A. 结束程序

B. 构成空循环体

C. 语法错误

D. 只执行一次

## 常见失分点



本题考查“空语句陷阱”（空语句、while）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

紧随条件的分号就是循环体，因此后续语句不属于循环。

</details>
