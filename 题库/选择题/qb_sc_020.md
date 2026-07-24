<!-- question-meta
id: QB-SC-020
category: 选择题
chapters: 6
concepts: 字符串比较
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符串比较

## 题目

判断字符串 `s1` 是否大于 `s2`，正确条件是（ ）。

A. s1>s2

B. strcmp(s1,s2)

C. strcmp(s1,s2)>0

D. strcat(s1,s2)>0

## 常见失分点



本题考查“字符串比较”（字符串比较）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

`strcmp` 返回正数表示第一个字符串按字典序大于第二个。

</details>
