<!-- question-meta
id: QB-FB-019
category: 程序填空
chapters: 10
concepts: 文件写入
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 逐字符写文件

## 题目

补全文件打开判断、循环结束条件和写字符调用。

## 常见失分点

不要只填出能编译的表达式；还要验证边界和最终输出。

<details>
<summary>参考答案与解析</summary>

**各空答案：** 检查 `fp==NULL`；`fputc(ch,fp)`

代回后应检查初始化、循环边界和字符串结束符。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void){FILE *fp=tmpfile();if(fp==NULL)return 1;fputs("ABC",fp);fclose(fp);return 0;}
```
<!-- reference-c:end -->

</details>
