<!-- question-meta
id: QB-SC-027
category: 选择题
chapters: 9
concepts: 结构体指针
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 结构体指针成员

## 题目

若 `struct S s,*p=&s;`，访问成员 `x` 的正确写法是（ ）。

A. p.x

B. p->x

C. *p.x

D. &p.x

## 常见失分点



本题考查“结构体指针成员”（结构体指针）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

`p` 是结构体指针，应使用箭头运算符。

</details>
