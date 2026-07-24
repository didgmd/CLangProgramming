<!-- question-meta
id: QB-FB-018
category: 程序填空
chapters: 6
concepts: 字符串输入
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 限制长度读取单词

## 题目

补全格式串，使长度为10的数组最多读入9个字符。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `scanf("%9s",s)`

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
