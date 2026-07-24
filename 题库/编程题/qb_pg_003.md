<!-- question-meta
id: QB-PG-003
category: 编程题
chapters: 4
concepts: 条件、闰年
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 判断闰年

## 题目

输入年份，判断是否为闰年。

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
int main(void){int y;if(scanf("%d",&y)!=1)return 1;puts(y%400==0||(y%4==0&&y%100!=0)?"leap":"common");return 0;}
```
<!-- reference-c:end -->

</details>
