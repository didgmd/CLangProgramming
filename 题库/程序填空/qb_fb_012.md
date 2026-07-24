<!-- question-meta
id: QB-FB-012
category: 程序填空
chapters: 5
concepts: 素数、嵌套循环
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 输出区间素数

## 题目

补全对每个候选数的试除与输出条件。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** 无因数时保持素数标志并输出

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){int n=29,p=n>=2;for(int i=2;i<=n/i&&p;i++)if(n%i==0)p=0;printf("%d\n",p);return 0;}
```
<!-- reference-c:end -->

</details>
