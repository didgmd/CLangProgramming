<!-- question-meta
id: QB-TR-022
category: 读程序写结果
chapters: 5、6
concepts: continue、break、二维数组
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 遇零跳出内层

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int a[2][4]={{1,2,-3,4},{5,0,7,8}},s=0;for(int i=0;i<2;i++)for(int j=0;j<4;j++){if(a[i][j]<0)continue;if(a[i][j]==0)break;s+=a[i][j];}printf("%d\n",s);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
12
```

第一行累加 1、2、4，第二行只累加 5 后遇零结束。

</details>
