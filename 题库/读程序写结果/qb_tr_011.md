<!-- question-meta
id: QB-TR-011
category: 读程序写结果
chapters: 6
concepts: 二维数组、求和
difficulty: 常规
minutes: 6
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# 矩阵非对角线求和

## 题目

写出程序的准确输出：

```c
#include <stdio.h>
int main(void){int a[3][3]={{3,4,5},{7,8,9},{10,11,12}},s=0;for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(i!=j)s+=a[i][j];printf("%d\n",s);return 0;}
```

## 常见失分点

按语句顺序记录变量变化；不要把赋值 `=` 看成比较 `==`。

<details>
<summary>参考答案与解析</summary>

**输出：**

```text
46
```

只累加非主对角线元素 4、5、7、9、10、11。

</details>
