<!-- question-meta
id: QB-SC-036
category: 选择题
chapters: 3
concepts: scanf、格式串
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# scanf格式匹配

## 题目

语句 `scanf("x=%f,y=%f",&x,&y);` 要求输入（ ）。

A. 2.5 2.5

B. 2.5,2.5

C. x=2.5,y=2.5

D. X=2.5,Y=2.5

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

格式串中的普通字符必须由输入原样匹配。

</details>
