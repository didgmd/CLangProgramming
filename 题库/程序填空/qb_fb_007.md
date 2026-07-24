<!-- question-meta
id: QB-FB-007
category: 程序填空
chapters: 6
concepts: 字符分类、计数
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 字符分类统计

## 题目

补全字母、数字、空格和其他字符四类统计条件。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** 字母范围；数字范围；空格比较；其他分支

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){char s[]="C 2026!";int a[4]={0};for(int i=0;s[i];i++){if((s[i]>='a'&&s[i]<='z')||(s[i]>='A'&&s[i]<='Z'))a[0]++;else if(s[i]>='0'&&s[i]<='9')a[1]++;else if(s[i]==' ')a[2]++;else a[3]++;}for(int i=0;i<4;i++)printf("%d%c",a[i],i==3?'\n':' ');return 0;}
```
<!-- reference-c:end -->

</details>
