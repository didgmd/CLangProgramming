<!-- question-meta
id: QB-PG-011
category: 编程题
chapters: 5
concepts: 循环、数位分解
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 水仙花数

## 题目

输出全部三位水仙花数。

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
int main(void){for(int n=100;n<=999;n++){int a=n/100,b=n/10%10,c=n%10;if(a*a*a+b*b*b+c*c*c==n)printf("%d ",n);}putchar('\n');return 0;}
```
<!-- reference-c:end -->

</details>
