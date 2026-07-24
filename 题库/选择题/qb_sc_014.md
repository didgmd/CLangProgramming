<!-- question-meta
id: QB-SC-014
category: 选择题
chapters: 6
concepts: 二维数组、边界
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 二维数组边界

## 题目

定义 `int a[3][4];` 后，正确的元素引用是（ ）。

A. a[1,2]

B. a[1][4]

C. a[1][1+2]

D. a(1)(3)

## 常见失分点



本题考查“二维数组边界”（二维数组、边界）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

列下标有效范围是 0～3，`1+2` 的结果为 3；其余写法越界或语法错误。

</details>
