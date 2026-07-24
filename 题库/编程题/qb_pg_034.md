<!-- question-meta
id: QB-PG-034
category: 编程题
chapters: 5
concepts: 素数、格式控制
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 指定区间输出素数

## 题目

输出100到200之间的素数并控制每行数量。

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
int main(void){int count=0;for(int n=100;n<=200;n++){int p=1;for(int i=2;i<=n/i&&p;i++)if(n%i==0)p=0;if(p){printf("%d%c",n,++count%5?' ':'\n');}}if(count%5)putchar('\n');return 0;}
```
<!-- reference-c:end -->

</details>
