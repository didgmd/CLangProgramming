<!-- question-meta
id: QB-SC-062
category: 选择题
chapters: 4
concepts: 短路求值
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 逻辑短路

## 题目

表达式 `a!=0 && b/a>1` 在 `a==0` 时（ ）。

A. 仍计算 b/a

B. 短路，不计算 b/a

C. 编译错误

D. 结果为真

## 常见失分点



本题考查“逻辑短路”（短路求值）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

`&&` 左侧为假时整体必假，右侧不会求值，从而避免除零。

</details>
