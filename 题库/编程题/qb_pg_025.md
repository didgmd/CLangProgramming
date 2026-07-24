<!-- question-meta
id: QB-PG-025
category: 编程题
chapters: 4、6
concepts: 日期、闰年
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 日期合法性与序号

## 题目

输入年月日，先验证日期，再计算当年第几天。

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
int main(void){int y,m,d;if(scanf("%d%d%d",&y,&m,&d)!=3)return 1;int days[]={0,31,28,31,30,31,30,31,31,30,31,30,31};if(y%400==0||(y%4==0&&y%100!=0))days[2]=29;if(m<1||m>12||d<1||d>days[m]){puts("invalid");return 0;}int sum=d;for(int i=1;i<m;i++)sum+=days[i];printf("%d\n",sum);return 0;}
```
<!-- reference-c:end -->

</details>
