<!-- question-meta
id: QB-FB-014
category: 程序填空
chapters: 6
concepts: 字符串、数值转换
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 数字字符串转整数

## 题目

补全符号处理和 `n=n*10+____`。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** `s[i]-'0'`；最终乘 `sign`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){char s[]="-23456";int i=0,sign=1,n=0;if(s[i]=='+'||s[i]=='-')sign=s[i++]=='+'?1:-1;while(s[i]>='0'&&s[i]<='9')n=n*10+s[i++]-'0';printf("%d\n",sign*n);return 0;}
```
<!-- reference-c:end -->

</details>
