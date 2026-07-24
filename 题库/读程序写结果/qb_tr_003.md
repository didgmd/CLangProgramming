<!-- question-meta
id: QB-TR-003
category: 读程序写结果
chapters: 5
concepts: for、continue、自减
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 循环中的自减与continue

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int y=9;for(;y>0;y--)if(y%3==0){printf("%d",--y);continue;}return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
852
```

命中 9、6、3 时先在输出表达式中自减，再执行循环更新。

</details>
