<!-- question-meta
id: QB-PG-002
category: 编程题
chapters: 6
concepts: 数组、最大值
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 十个数中的最大值

## 题目

输入10个数，输出最大值。

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
int main(void){double a[10];for(int i=0;i<10;i++)if(scanf("%lf",&a[i])!=1)return 1;double m=a[0];for(int i=1;i<10;i++)if(a[i]>m)m=a[i];printf("%.6f\n",m);return 0;}
```
<!-- reference-c:end -->

</details>
