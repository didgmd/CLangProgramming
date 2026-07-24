<!-- question-meta
id: QB-PG-012
category: 编程题
chapters: 6
concepts: 字符串、状态
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 统计一行中的单词数

## 题目

输入一行字符，统计由空白分隔的单词个数。

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
int main(void){char s[256];if(!fgets(s,sizeof s,stdin))return 1;int count=0,in=0;for(int i=0;s[i];i++){int blank=s[i]==' '||s[i]=='\t'||s[i]=='\n';if(!blank&&!in){count++;in=1;}else if(blank)in=0;}printf("%d\n",count);return 0;}
```
<!-- reference-c:end -->

</details>
