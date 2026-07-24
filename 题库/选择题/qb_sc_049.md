<!-- question-meta
id: QB-SC-049
category: 选择题
chapters: 8
concepts: 数组名、指针
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 数组名自增

## 题目

已定义 `char a[10];`，表达式 `a++`（ ）。

A. 合法并移动数组

B. 非法，数组名不可修改

C. 把首字符加一

D. 清空数组

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

数组名在表达式中常转换为首元素地址，但本身不是可修改左值。

</details>
