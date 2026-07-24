<!-- question-meta
id: QB-SC-048
category: 选择题
chapters: 8
concepts: 指针运算
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符串指针移动

## 题目

`char *p=str; p++;` 的作用是（ ）。

A. 修改首字符

B. 让 p 指向下一个字符

C. 删除字符串

D. 移动数组本体

## 常见失分点



本题考查“字符串指针移动”（指针运算）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：B。**

自增改变指针保存的地址，使其指向下一个元素。

</details>
