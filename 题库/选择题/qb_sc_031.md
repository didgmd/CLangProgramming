<!-- question-meta
id: QB-SC-031
category: 选择题
chapters: 10
concepts: 转义字符、文件路径
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# Windows路径字符串

## 题目

要表示路径 `D:\program\file.txt`，正确的 C 字符串是（ ）。

A. "D:\program\file.txt"

B. "D:\\program\\file.txt"

C. "D:/program\file.txt"

D. "D:program:file.txt"

## 常见失分点



本题考查“Windows路径字符串”（转义字符、文件路径）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

反斜杠在字符串中需要写成 `\\`。

</details>
