<!-- question-meta
id: QB-PG-014
category: 编程题
chapters: 5
concepts: 数位分解
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 四位数各位立方和

## 题目

输入四位正整数，求各位数字立方和。

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
int main(void){int n;if(scanf("%d",&n)!=1||n<1000||n>9999){puts("invalid");return 0;}int sum=0;for(int x=n;x;x/=10){int d=x%10;sum+=d*d*d;}printf("%d\n",sum);return 0;}
```
<!-- reference-c:end -->

</details>
