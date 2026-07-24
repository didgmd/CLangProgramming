<!-- question-meta
id: QB-PG-004
category: 编程题
chapters: 6
concepts: 冒泡排序
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 十个整数冒泡排序

## 题目

输入10个整数，使用冒泡法升序输出。

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
int main(void){int a[10];for(int i=0;i<10;i++)if(scanf("%d",&a[i])!=1)return 1;for(int j=0;j<9;j++)for(int i=0;i<9-j;i++)if(a[i]>a[i+1]){int t=a[i];a[i]=a[i+1];a[i+1]=t;}for(int i=0;i<10;i++)printf("%d%c",a[i],i==9?'\n':' ');return 0;}
```
<!-- reference-c:end -->

</details>
