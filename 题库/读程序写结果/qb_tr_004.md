<!-- question-meta
id: QB-TR-004
category: 读程序写结果
chapters: 5、6
concepts: 字符输入、循环
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符结束标志

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int c;while((c=getchar())!='$'&&c!=EOF)putchar(c);printf("End!\n");return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
abcdefgEnd!
```

输入 `abcdefg$abcdefg` 时，美元符号后的字符不再处理。

</details>
