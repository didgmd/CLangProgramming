<!-- question-meta
id: QB-TR-013
category: 读程序写结果
chapters: 4
concepts: 逻辑与、if
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 逻辑与分支

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int x=2,y=3,z=4;if(x<y&&y<z)x+=z;else y-=x;printf("%d\n",x+y);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
9
```

两个关系均为真，`x` 变为 6，再与 `y` 相加。

</details>
