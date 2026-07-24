<!-- question-meta
id: QB-PG-017
category: 编程题
chapters: 7、8
concepts: 字符串复制、指针
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 不用字符串库复制

## 题目

输入一行字符串，调用自定义函数复制并输出。

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
static void copy_string(const char *a,char *b){while((*b++=*a++)!='\0'){} }
int main(void){char a[80],b[80];if(!fgets(a,sizeof a,stdin))return 1;copy_string(a,b);printf("%s",b);return 0;}
```
<!-- reference-c:end -->

</details>
