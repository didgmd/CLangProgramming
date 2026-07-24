<!-- question-meta
id: QB-TR-005
category: 读程序写结果
chapters: 6
concepts: 数组、循环
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 数组累加

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int a[10],k=0;for(int i=0;i<10;i++)a[i]=i;for(int i=1;i<4;i++)k+=a[i]+i;printf("%d\n",k);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
12
```

三次分别累加 2、4、6。

</details>
