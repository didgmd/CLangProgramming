<!-- question-meta
id: QB-SC-022
category: 选择题
chapters: 8
concepts: 数组名、指针
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 数组名不可赋值

## 题目

下列赋值错误的是（ ）。

A. char *p="abc";

B. char a[4]; a[0]='a';

C. char a[4]; a="abc";

D. char a[]="abc";

## 常见失分点



本题考查“数组名不可赋值”（数组名、指针）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

数组名不是可修改左值，数组定义完成后不能用赋值号整体接收字符串。

</details>
