<!-- question-meta
id: QB-TR-008
category: 读程序写结果
chapters: 6
concepts: 字符串、数值转换
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 带符号数字转换

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){char s[]="-12345";int k=0,sign=1,m=0;if(s[k]=='+'||s[k]=='-')sign=s[k++]=='+'?1:-1;for(;s[k]>='0'&&s[k]<='9';k++)m=m*10+s[k]-'0';printf("Result=%d\n",sign*m);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
Result=-12345
```

先记录负号，再逐位构造整数。

</details>
