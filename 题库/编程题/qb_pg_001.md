<!-- question-meta
id: QB-PG-001
category: 编程题
chapters: 4
concepts: 分支、浮点运算
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 一元二次方程

## 题目

输入三个实数系数，完整处理退化、重根、两个实根和复根。

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
#include <math.h>
#include <stdio.h>
int main(void){double a,b,c;if(scanf("%lf%lf%lf",&a,&b,&c)!=3)return 1;if(fabs(a)<1e-12){if(fabs(b)<1e-12)puts(fabs(c)<1e-12?"any":"none");else printf("%.6f\n",-c/b);return 0;}double d=b*b-4*a*c;if(d>1e-12)printf("%.6f %.6f\n",(-b+sqrt(d))/(2*a),(-b-sqrt(d))/(2*a));else if(fabs(d)<=1e-12)printf("%.6f\n",-b/(2*a));else printf("%.6f+%.6fi %.6f-%.6fi\n",-b/(2*a),sqrt(-d)/fabs(2*a),-b/(2*a),sqrt(-d)/fabs(2*a));return 0;}
```
<!-- reference-c:end -->

</details>
