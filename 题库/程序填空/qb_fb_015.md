<!-- question-meta
id: QB-FB-015
category: 程序填空
chapters: 4、6
concepts: 条件、数组
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 统计负数

## 题目

输入10个整数，统计负数的个数并计算负数之和。

输入：10个整数；输出：负数个数与负数之和。

```c
#include <stdio.h>
int main(void)
{
    int /*〔1〕*/, /*〔2〕*/;
    for (int i = 0, x; i < 10; i++)
    {
        if (scanf("%d", &x) != 1)
        return 1;
        if ( /*〔3〕*/ )
        {
            /*〔4〕*/;
            /*〔5〕*/;
        }
    }
    printf("%d %d\n", count, sum);
    return 0;
}
```

## 常见失分点


本题围绕“统计负数”补全条件、数组相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`count=0`
2. `〔2〕`：`sum=0`
3. `〔3〕`：`x<0`
4. `〔4〕`：`count++`
5. `〔5〕`：`sum+=x`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：无负数时应输出 `0 0`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int count = 0, sum = 0;
    for (int i = 0, x; i < 10; i++)
    {
        if (scanf("%d", &x) != 1)
        {
            return 1;
        }
        if (x < 0)
        {
            count++;
            sum += x;
        }
    }
    printf("%d %d\n", count, sum);
    return 0;
}
```
<!-- reference-c:end -->

</details>
