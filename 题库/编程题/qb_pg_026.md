<!-- question-meta
id: QB-PG-026
category: 编程题
chapters: 6
concepts: 字符串、溢出
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 带校验的字符串转整数

## 题目

转换带可选符号的十进制字符串，并识别非法输入及溢出。

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
#include <limits.h>
#include <stdio.h>
int main(void){char s[64];if(scanf("%63s",s)!=1)return 1;int i=0,sign=1;if(s[i]=='+'||s[i]=='-')sign=s[i++]=='-'?-1:1;if(!s[i]){puts("invalid");return 0;}long long n=0;for(;s[i];i++){if(s[i]<'0'||s[i]>'9'){puts("invalid");return 0;}n=n*10+s[i]-'0';if((sign==1&&n>INT_MAX)||(sign==-1&&-n<INT_MIN)){puts("overflow");return 0;}}printf("%lld\n",sign*n);return 0;}
```
<!-- reference-c:end -->

</details>
