<!-- question-meta
id: QB-FB-022
category: 程序填空
chapters: 8
concepts: 指针复位
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 遍历指针重新定位

## 题目

指针移动到数组尾后，补全重新定位语句，再次顺序输出数组。

无输入；输出：`3 6 9`。

```c
#include <stdio.h>
int main(void)
{
    int a [3] =
    {
        3, 6, 9
    }
    ;
    int *
    /*〔1〕*/
    ;
    while(p < a + 3) p++;
    p = a;
    while(p < a + 3)
    {
        printf("%d%c", * p, p == a + 2 ? '\n' : ' ');
        p++;
    }
    return 0;
}
```

## 常见失分点


本题围绕“遍历指针重新定位”补全指针复位相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`p=a`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：移动后的指针可比较，但在重新指向数组元素前不得解引用。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int a [3] =
    {
        3, 6, 9
    }
    ;
    int * p = a;
    while(p < a + 3) p++;
    p = a;
    while(p < a + 3)
    {
        printf("%d%c", * p, p == a + 2 ? '\n' : ' ');
        p++;
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
