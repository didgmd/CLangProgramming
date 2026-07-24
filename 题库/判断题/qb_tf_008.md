<!-- question-meta
id: QB-TF-008
category: 判断题
chapters: 8
concepts: 数组名、指针
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 数组名可以自增

## 题目

判断下列说法是否正确：

> 若 `p` 是指针变量、`a` 是数组名，则 `p++` 和 `a++` 都合法。

## 常见失分点



判断“数组名可以自增”时应先确认命题前提（数组名、指针），再用规则或反例检验其中的绝对表述。

<details>
<summary>参考答案与解析</summary>

**答案：错误。**

**正确表述：** `p` 可修改，而数组名不是可修改左值。

</details>
