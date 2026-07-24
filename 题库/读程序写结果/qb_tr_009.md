<!-- question-meta
id: QB-TR-009
category: 读程序写结果
chapters: 6
concepts: 二维字符数组、字符串
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 二维字符数组后缀

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
#include <string.h>
int main(void){char ch[]="abc",x[3][4];for(int i=0;i<3;i++)strcpy(x[i],ch);for(int i=0;i<3;i++)printf("%s",&x[i][i]);putchar('\n');return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
abcbcc
```

三次输出的后缀依次为 `abc`、`bc`、`c`。

</details>
