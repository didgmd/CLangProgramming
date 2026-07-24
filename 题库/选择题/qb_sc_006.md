<!-- question-meta
id: QB-SC-006
category: 选择题
chapters: 3
concepts: 自增运算符
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 后缀自增

## 题目

已知 `int j, i=1;`，执行 `j=i++;` 后，`i` 的值是（ ）。

A. 1

B. 2

C. -1

D. -2

## 常见失分点



本题考查“后缀自增”（自增运算符）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

后缀自增先把旧值赋给 `j`，随后 `i` 增加为 2。

</details>
