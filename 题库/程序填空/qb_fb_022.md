<!-- question-meta
id: QB-FB-022
category: 程序填空
chapters: 8
concepts: 指针复位
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 遍历指针重新定位

## 题目

完成一次 `while(p<a+n) p++;` 后，如需重新输出数组，应补全 `____`。

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
