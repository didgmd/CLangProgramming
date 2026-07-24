<!-- question-meta
id: QB-TR-019
category: 读程序写结果
chapters: 4
concepts: 条件运算符
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 三目运算符求大值

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int a=3,b=4,c=6;int d=a>b?(a>c?a:c):b;printf("%d\n",d);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
4
```

由于 `a>b` 为假，整个条件表达式直接取 `b`。

</details>
