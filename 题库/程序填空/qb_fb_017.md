<!-- question-meta
id: QB-FB-017
category: 程序填空
chapters: 3
concepts: 字符编码
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 字符大小写转换

## 题目

补全两个字符变量、字符常量和大小写差值。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `b`；`'a'`；`32`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){int n[26]={0},c;while((c=getchar())!='#'&&c!=EOF)if(c>='A'&&c<='Z')n[c-'A']++;for(int i=0;i<26;i++)printf("%c:%d\n",'A'+i,n[i]);return 0;}
```
<!-- reference-c:end -->

</details>
