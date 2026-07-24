<!-- question-meta
id: QB-FB-015
category: 程序填空
chapters: 4、6
concepts: 条件、数组
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 统计负数

## 题目

补全计数器初始化、负数条件和累加语句。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `sum=count=0`；`a[i]<0`；`sum+=a[i]`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){int a[7]={12,9,16,5,7,2,1};for(int k=0;k<7/2;k++){int t=a[k];a[k]=a[6-k];a[6-k]=t;}for(int k=0;k<7;k++)printf("%d%c",a[k],k==6?'\n':' ');return 0;}
```
<!-- reference-c:end -->

</details>
