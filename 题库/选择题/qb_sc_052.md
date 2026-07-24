<!-- question-meta
id: QB-SC-052
category: 选择题
chapters: 6
concepts: 二维数组初始化
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 二维数组省略行数

## 题目

完整初始化二维数组时（ ）。

A. 可省略行数但不能省略列数

B. 可省略列数

C. 行列均可省略

D. 均不能省略

## 常见失分点



本题考查“二维数组省略行数”（二维数组初始化）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：A。**

编译器可由初始化项推断行数，但必须知道每行列数。

</details>
