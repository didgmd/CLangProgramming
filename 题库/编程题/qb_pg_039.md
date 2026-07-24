<!-- question-meta
id: QB-PG-039
category: 编程题
chapters: 5
concepts: 二分查找、整数溢出
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 非负整数平方根整数部分

## 题目

输入非负整数，用二分查找输出平方根的整数部分。

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
int main(void){unsigned n;if(scanf("%u",&n)!=1)return 1;unsigned lo=0,hi=n<65535?n:65535,ans=0;while(lo<=hi){unsigned mid=lo+(hi-lo)/2;if(mid==0||mid<=n/mid){ans=mid;lo=mid+1;}else hi=mid-1;}printf("%u\n",ans);return 0;}
```
<!-- reference-c:end -->

</details>
