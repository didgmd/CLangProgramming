<!-- question-meta
id: QB-SC-038
category: 选择题
chapters: 6
concepts: 字符串输入、安全输入
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 读取含空格文本

## 题目

现代 C 程序需要读取一整行且可能含空格时，优先使用（ ）。

A. scanf("%s")

B. getchar()

C. fgets()

D. putchar()

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

`fgets` 可限制缓冲区长度并读取空格；`scanf("%s")` 遇空白停止。

</details>
