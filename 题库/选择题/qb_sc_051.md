<!-- question-meta
id: QB-SC-051
category: 选择题
chapters: 6
concepts: 字符数组初始化
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符数组初始化

## 题目

`char c[]="Very Good";`（ ）。

A. 是合法初始化

B. 因空格而非法

C. 缺少长度必定错误

D. 不能含大写字母

## 常见失分点



本题考查“字符数组初始化”（字符数组初始化）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：A。**

编译器会按字符串长度自动确定数组大小并加入结束符。

</details>
