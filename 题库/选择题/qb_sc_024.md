<!-- question-meta
id: QB-SC-024
category: 选择题
chapters: 8
concepts: 二级指针
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 二级指针解引用

## 题目

已知 `int i=100,*j=&i,**k=&j;`，表达式 `**k` 的值是（ ）。

A. 运行错误

B. 100

C. i 的地址

D. j 的地址

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

第一次解引用得到 `j`，第二次解引用得到 `i` 的值 100。

</details>
