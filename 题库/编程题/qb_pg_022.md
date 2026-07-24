<!-- question-meta
id: QB-PG-022
category: 编程题
chapters: 6
concepts: 选择排序、成绩数组
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 成绩选择排序

## 题目

输入10个学生成绩，使用选择排序升序输出。

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
int main(void){int a[10];for(int i=0;i<10;i++)if(scanf("%d",&a[i])!=1)return 1;for(int i=0;i<9;i++){int k=i;for(int j=i+1;j<10;j++)if(a[j]<a[k])k=j;int t=a[i];a[i]=a[k];a[k]=t;}for(int i=0;i<10;i++)printf("%d%c",a[i],i==9?'\n':' ');return 0;}
```
<!-- reference-c:end -->

</details>
