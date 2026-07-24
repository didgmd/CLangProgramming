<!-- question-meta
id: QB-FB-020
category: 程序填空
chapters: 8
concepts: 指针移动、指针复位
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 指针遍历后复位

## 题目

指针遍历数组后还需从首元素再次访问，应补写什么？

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `p=a;`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){int a[]={1,2,3,4},*p=a;while(p<a+4)printf("%d ",*p++);p=a;printf("\n%d\n",*p);return 0;}
```
<!-- reference-c:end -->

</details>
