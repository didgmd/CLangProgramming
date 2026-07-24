<!-- question-meta
id: QB-TR-029
category: 读程序写结果
chapters: 6
concepts: 选择排序
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 选择排序第一轮

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int a[5]={4,2,5,1,3},k=0;for(int j=1;j<5;j++)if(a[j]<a[k])k=j;int t=a[0];a[0]=a[k];a[k]=t;for(int i=0;i<5;i++)printf("%d ",a[i]);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
1 2 5 4 3 
```

第一轮找到最小值 1，并与下标 0 的元素交换。

</details>
