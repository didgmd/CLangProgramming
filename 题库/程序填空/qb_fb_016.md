<!-- question-meta
id: QB-FB-016
category: 程序填空
chapters: 6
concepts: 字符串、逆序
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 字符串正序后接逆序

## 题目

补全字符串长度、逆序下标和新串结束符。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `strlen(s)`；`s[n-1-i]`；`'\0'`

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
