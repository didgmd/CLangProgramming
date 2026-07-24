<!-- question-meta
id: QB-TR-021
category: 读程序写结果
chapters: 6
concepts: 字符串、字符替换
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 字符替换下标

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){char s[]="Ah2MA";for(int i=0;s[i];i++){if(s[i]=='a')s[i]='A';else if(s[i]=='A')s[i]='a';}puts(s);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
ah2Ma
```

所有 `A` 与 `a` 互换，其他字符不变。

</details>
