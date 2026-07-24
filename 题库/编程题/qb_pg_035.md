<!-- question-meta
id: QB-PG-035
category: 编程题
chapters: 6
concepts: 字符分类
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 一行字符分类统计

## 题目

统计字母、数字、空格和其他字符，忽略结尾换行。

## 常见失分点

避免只写核心循环而遗漏输入检查、初始化、边界和输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 先明确输入、边界和输出，再把处理过程拆成可检查的步骤。

**评分建议：** 输入与边界 2 分，核心算法 5 分，输出 2 分，代码规范 1 分。

**测试建议：** 至少覆盖正常值、边界值和一个容易出错的输入。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){char s[256];if(!fgets(s,sizeof s,stdin))return 1;int a=0,d=0,sp=0,o=0;for(int i=0;s[i]&&s[i]!='\n';i++){if((s[i]>='a'&&s[i]<='z')||(s[i]>='A'&&s[i]<='Z'))a++;else if(s[i]>='0'&&s[i]<='9')d++;else if(s[i]==' ')sp++;else o++;}printf("%d %d %d %d\n",a,d,sp,o);return 0;}
```
<!-- reference-c:end -->

</details>
