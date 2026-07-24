<!-- question-meta
id: QB-FB-005
category: 程序填空
chapters: 6
concepts: 数组逆序
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 数组逆序

## 题目

补全首尾交换循环的自增、临时变量回写和输出下标。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `k++`；`t`；`a[k]`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){int a[7]={12,9,16,5,7,2,1};for(int k=0;k<7/2;k++){int t=a[k];a[k]=a[6-k];a[6-k]=t;}for(int k=0;k<7;k++)printf("%d%c",a[k],k==6?'\n':' ');return 0;}
```
<!-- reference-c:end -->

</details>
