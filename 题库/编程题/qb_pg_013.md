<!-- question-meta
id: QB-PG-013
category: 编程题
chapters: 6、7
concepts: 冒泡排序、函数
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 浮点数组子函数排序

## 题目

输入10个浮点数，调用排序子函数按升序输出。

## 常见失分点

避免只写核心循环而遗漏输入检查、初始化、边界和输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 先明确输入、边界和输出，再把处理过程拆成可检查的步骤。

**评分建议：** 输入与边界 2 分，核心算法 5 分，输出 2 分，代码规范 1 分。

**测试建议：** 至少覆盖正常值、边界值和一个容易出错的输入。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
static void sort(double a[],int n){for(int j=0;j<n-1;j++)for(int i=0;i<n-1-j;i++)if(a[i]>a[i+1]){double t=a[i];a[i]=a[i+1];a[i+1]=t;}}
int main(void){double a[10];for(int i=0;i<10;i++)if(scanf("%lf",&a[i])!=1)return 1;sort(a,10);for(int i=0;i<10;i++)printf("%.2f%c",a[i],i==9?'\n':' ');return 0;}
```
<!-- reference-c:end -->

</details>
