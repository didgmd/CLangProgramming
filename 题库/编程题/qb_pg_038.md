<!-- question-meta
id: QB-PG-038
category: 编程题
chapters: 8
concepts: 字符指针、指针差
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 指针法求字符串长度

## 题目

不调用 `strlen`，使用两个指针之差求字符串长度。

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
static int length(const char *s){const char *p=s;while(*p)p++;return (int)(p-s);}
int main(void){char s[128];if(!fgets(s,sizeof s,stdin))return 1;int n=length(s);if(n>0&&s[n-1]=='\n')n--;printf("%d\n",n);return 0;}
```
<!-- reference-c:end -->

</details>
