<!-- question-meta
id: QB-FB-003
category: 程序填空
chapters: 6、7
concepts: 冒泡排序、函数
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 冒泡排序

## 题目

补全外层范围、内层范围、比较条件和排序函数调用。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `j<n-1`；`i<n-1-j`；`a[i]>a[i+1]`；`sort(a,10)`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
static void sort(int a[],int n){for(int j=0;j<n-1;j++)for(int i=0;i<n-1-j;i++)if(a[i]>a[i+1]){int t=a[i];a[i]=a[i+1];a[i+1]=t;}}
int main(void){int a[10]={3,7,5,1,2,8,6,4,10,9};sort(a,10);for(int i=0;i<10;i++)printf("%d%c",a[i],i==9?'\n':' ');return 0;}
```
<!-- reference-c:end -->

</details>
