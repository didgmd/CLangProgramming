<!-- question-meta
id: QB-SC-029
category: 选择题
chapters: 10
concepts: 文件指针
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 文件指针定义

## 题目

正确定义文件指针 `fp` 的语句是（ ）。

A. FILE fp;

B. file *fp;

C. FILE *fp;

D. file fp;

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

`FILE` 是标准库类型，文件操作使用 `FILE *`。

</details>
