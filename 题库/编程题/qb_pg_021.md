<!-- question-meta
id: QB-PG-021
category: 编程题
chapters: 6
concepts: 二维数组、矩阵转置
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 三阶矩阵转置

## 题目

输入3阶矩阵，将转置结果保存到另一矩阵并输出。

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
int main(void){int a[3][3],b[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(scanf("%d",&a[i][j])!=1)return 1;for(int i=0;i<3;i++)for(int j=0;j<3;j++)b[j][i]=a[i][j];for(int i=0;i<3;i++){for(int j=0;j<3;j++)printf("%d%c",b[i][j],j==2?'\n':' ');}return 0;}
```
<!-- reference-c:end -->

</details>
