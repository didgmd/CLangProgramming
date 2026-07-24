<!-- question-meta
id: QB-SC-003
category: 选择题
chapters: 3
concepts: 常量、转义字符
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 合法常量

## 题目

下列选项中不能作为 C 语言合法常量的是（ ）。

A. 'cd'

B. 0.1e+6

C. "\a"

D. '\011'

## 常见失分点



本题考查“合法常量”（常量、转义字符）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：A。**

字符常量通常表示一个字符；`'cd'` 是多字符常量，不能按本课程的单字符常量规则使用。

</details>
