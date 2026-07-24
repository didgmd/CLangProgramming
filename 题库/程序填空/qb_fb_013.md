<!-- question-meta
id: QB-FB-013
category: 程序填空
chapters: 5、7
concepts: 函数、浮点运算
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 调和级数分组求和

## 题目

补全函数内 `1.0/i` 累加和主函数中的函数调用。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `s+=1.0/i`；`sum+=f(i)`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
static double f(int n){double s=0;for(int i=1;i<=n;i++)s+=1.0/i;return s;}
int main(void){double sum=0;for(int i=1;i<=3;i++)sum+=f(i);printf("%.6f\n",sum);return 0;}
```
<!-- reference-c:end -->

</details>
