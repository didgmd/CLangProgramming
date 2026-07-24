<!-- question-meta
id: QB-SC-047
category: 选择题
chapters: 6
concepts: 二维数组
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 二维数组线性位置

## 题目

二维数组每行有 `m` 列，`a[i][j]` 前面共有（ ）个元素。

A. j*m+i

B. i*m+j

C. i*m+j-1

D. i+j

## 常见失分点



本题考查“二维数组线性位置”（二维数组）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

前面有 `i` 个完整行，共 `i*m` 个，再加本行前面的 `j` 个。

</details>
