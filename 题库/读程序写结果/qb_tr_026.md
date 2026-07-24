<!-- question-meta
id: QB-TR-026
category: 读程序写结果
chapters: 7
concepts: 递归、阶乘
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 递归阶乘

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
static long long f(int n){return n<=1?1:n*f(n-1);}
int main(void){printf("%lld\n",f(5));return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
120
```

递归展开为 `5*4*3*2*1`。

</details>
