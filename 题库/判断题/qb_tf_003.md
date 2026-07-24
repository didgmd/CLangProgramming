<!-- question-meta
id: QB-TF-003
category: 判断题
chapters: 6
concepts: 二维数组初始化
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 二维数组部分初始化

## 题目

判断下列说法是否正确：

> `int a[3][4]={{1},{5},{9}};` 会把每行首元素分别初始化为 1、5、9，其余元素置 0。

## 常见失分点

判断题要关注“只能”“必须”“所有”等绝对化措辞。

<details>
<summary>参考答案与解析</summary>

**答案：正确。**

聚合类型未显式给出的元素执行零初始化。

</details>
