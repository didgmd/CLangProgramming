<!-- question-meta
id: QB-PG-040
category: 编程题
chapters: 6、7
concepts: 二维数组、函数化
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 函数化杨辉三角

## 题目

把递推和输出步骤组织成清晰模块，输出给定行数的杨辉三角。

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
#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
int main(void){int n;if(scanf("%d",&n)!=1||n<1||n>20)return 1;long long a[20][20]={{0}};for(int i=0;i<n;i++){a[i][0]=a[i][i]=1;for(int j=1;j<i;j++)a[i][j]=a[i-1][j-1]+a[i-1][j];for(int j=0;j<=i;j++)printf("%lld%c",a[i][j],j==i?'\n':' ');}return 0;}
```
<!-- reference-c:end -->

</details>
