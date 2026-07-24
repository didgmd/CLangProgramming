<!-- question-meta
id: QB-SC-010
category: 选择题
chapters: 4
concepts: switch、贯穿
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# switch贯穿

## 题目

若 `i=10`，执行无 `break` 的 `switch`：`case 10:i++; case 11:i++; default:i++;` 后，`i` 为（ ）。

A. 10

B. 11

C. 12

D. 13

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：D。**

从 `case 10` 进入后连续执行后续两个分支，因此共增加 3。

</details>
