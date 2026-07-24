<!-- question-meta
id: QB-PG-028
category: 编程题
chapters: 7
concepts: 递归、数组
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 递归生成斐波那契数组

## 题目

用递归函数生成并输出前20项。

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
static long long fib(int n){return n<2?n:fib(n-1)+fib(n-2);}
int main(void){for(int i=0;i<20;i++)printf("%lld%c",fib(i),i==19?'\n':' ');return 0;}
```
<!-- reference-c:end -->

</details>
