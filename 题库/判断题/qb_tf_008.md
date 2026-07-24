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

判断题要关注“只能”“必须”“所有”等绝对化措辞。

<details>
<summary>参考答案与解析</summary>

**答案：错误。**

`p` 可修改，而数组名不是可修改左值。

</details>
