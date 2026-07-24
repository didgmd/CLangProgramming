<!-- question-meta
id: QB-TR-010
category: 读程序写结果
chapters: 6
concepts: 数组、递推
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 递推数组

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int a[6];a[0]=5;for(int j=1;j<6;j++){a[j]=j*j+5;if(j>2)a[j]=2*a[j]-a[j-1];}for(int j=0;j<6;j++)printf("%d%c",a[j],j==5?'\n':' ');return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
5 6 9 19 23 37
```

从下标 3 开始应用第二个递推式。

</details>
