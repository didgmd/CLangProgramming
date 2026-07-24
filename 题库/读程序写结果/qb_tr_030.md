<!-- question-meta
id: QB-TR-030
category: 读程序写结果
chapters: 4
concepts: 短路求值
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 短路避免除零

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int a=0,b=5;if(a!=0&&b/a>1)puts("yes");else puts("no");return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
no
```

左操作数为假，右侧除法不求值。

</details>
