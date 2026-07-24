<!-- question-meta
id: QB-SC-023
category: 选择题
chapters: 8
concepts: 指针、scanf
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# scanf与指针

## 题目

已定义 `int a,*pa=&a;`，能正确读入 `a` 的语句是（ ）。

A. scanf("%d",pa);

B. scanf("%d",a);

C. scanf("%d",&pa);

D. scanf("%d",*pa);

## 常见失分点

先判断语法和运算规则，再看选项；不要只凭代码外观猜测。

<details>
<summary>参考答案与解析</summary>

**答案：A。**

`pa` 保存 `a` 的地址，正好满足 `%d` 所需的 `int *` 参数。

</details>
