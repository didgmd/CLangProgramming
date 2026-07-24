<!-- question-meta
id: QB-SC-063
category: 选择题
chapters: 3
concepts: 未定义行为、求值顺序
difficulty: 综合
minutes: 3
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 未定义求值顺序诊断

## 题目

表达式 `printf("%d %d", i++, i++);` 的输出应如何判断？

A. 总是先输出小值

B. 总是从右向左

C. 行为未定义，不能预测

D. 只与优化级别无关

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

两个对同一标量对象的修改之间没有规定的先后关系，不能把某次运行结果当作标准答案。

</details>
