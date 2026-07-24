<!-- question-meta
id: QB-TR-023
category: 读程序写结果
chapters: 6
concepts: 数字字符串
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符串数字转换前导零

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){char s[]="00124008";long n=0;for(int i=0;s[i];i++)n=n*10+s[i]-'0';printf("%ld\n",n);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
124008
```

按十进制累积时前导零不改变数值。

</details>
