<!-- question-meta
id: QB-TR-018
category: 读程序写结果
chapters: 8
concepts: 字符指针
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符指针后缀

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){char s[]="ABCD";for(char *p=s;*p;p++)printf("%s ",p);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
ABCD BCD CD D 
```

每次指针后移一位，`%s` 输出当前位置开始的后缀。

</details>
