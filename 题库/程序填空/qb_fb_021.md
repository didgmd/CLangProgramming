<!-- question-meta
id: QB-FB-021
category: 程序填空
chapters: 6
concepts: 杨辉三角、数组边界
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 杨辉三角边界诊断

## 题目

修正递推循环：两侧元素为1，内部循环必须避免访问上一行的负下标和本行之外元素。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `a[i][0]=a[i][i]=1`；内部 `1<=j<i`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){int a[7][7]={{0}};for(int i=0;i<7;i++){a[i][0]=a[i][i]=1;for(int j=1;j<i;j++)a[i][j]=a[i-1][j-1]+a[i-1][j];}for(int i=0;i<7;i++){for(int j=0;j<=i;j++)printf("%4d",a[i][j]);putchar('\n');}return 0;}
```
<!-- reference-c:end -->

</details>
