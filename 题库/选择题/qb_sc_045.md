<!-- question-meta
id: QB-SC-045
category: 选择题
chapters: 6
concepts: 字符串复制、数组容量
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符串复制空间

## 题目

把字符串 `HELLO2` 复制到 `char s[7]` 中（ ）。

A. 空间足够

B. 缺少结束符空间

C. 只能存两个字符

D. 必定编译错误

## 常见失分点



本题考查“字符串复制空间”（字符串复制、数组容量）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：A。**

6 个可见字符加一个 `\0` 正好需要 7 字节。

</details>
