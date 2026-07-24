<!-- question-meta
id: QB-FB-008
category: 程序填空
chapters: 7、8
concepts: 函数、字符指针
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 函数复制字符串

## 题目

补全 `while((____=____)!='\0')` 形式的复制循环。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `*to++`；`*from++`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
static void copy(const char *from,char *to){while((*to++=*from++)!='\0'){} }
int main(void){char a[]="programming",b[32];copy(a,b);puts(b);return 0;}
```
<!-- reference-c:end -->

</details>
