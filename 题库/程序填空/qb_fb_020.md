<!-- question-meta
id: QB-FB-020
category: 程序填空
chapters: 8
concepts: 指针移动、指针复位
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 指针遍历后复位

## 题目

指针完成一次数组遍历后，补全复位语句，使其再次从首元素访问。

无输入；输出：数组 `2 4 6 8`。

```c
#include <stdio.h>
int main(void)
{
    int a[4] = {2, 4, 6, 8};
    int *
    /*〔1〕*/;
    while (p < a + 4)
    p++;
    p = a;
    for (int i = 0; i < 4; i++)
    printf("%d%c", p[i], i == 3 ? '\n' : ' ');
    return 0;
}
```

## 常见失分点


本题围绕“指针遍历后复位”补全指针移动、指针复位相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`p=a`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：遍历结束时 `p==a+4`，不能解引用，必须先重新定位。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int a[4] = {2, 4, 6, 8};
    int * p = a;
    while (p < a + 4)
    {
        p++;
    }
    p = a;
    for (int i = 0; i < 4; i++)
    {
        printf("%d%c", p[i], i == 3 ? '\n' : ' ');
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
