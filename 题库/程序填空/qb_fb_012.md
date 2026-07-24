<!-- question-meta
id: QB-FB-012
category: 程序填空
chapters: 5
concepts: 素数、嵌套循环
difficulty: 常规
minutes: 8
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 输出区间素数

## 题目

补全程序，输出100到200之间的所有素数。

无输入；输出：100至200之间的素数。

```c
#include <stdio.h>
int main(void)
{
    for(int n = 100;
    /*〔1〕*/
    ; n++)
    {
        int prime = 1;
        for(int i = 2;
        /*〔2〕*/
        ; i++) if(
        /*〔3〕*/
        )
        {
            prime = 0;
            break;
        }
        /*〔4〕*/
        printf("%d ", n);
    }
    putchar('\n');
    return 0;
}
```

## 常见失分点


本题围绕“输出区间素数”补全素数、嵌套循环相关语句。各空代回后应共同检查初始化、循环边界、有效下标或指针范围以及最终输出。

<details>
<summary>参考答案与解析</summary>

### 各空答案

1. `〔1〕`：`n<=200`
2. `〔2〕`：`i*i<=n`
3. `〔3〕`：`n%i==0`
4. `〔4〕`：`if(prime)`

### 关键说明

将各空代回后，程序的声明、初始化、循环边界和输出应形成完整逻辑。验证数据：输出应从 `101` 开始，以 `199` 结束。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    for(int n = 100; n <= 200; n++)
    {
        int prime = 1;
        for(int i = 2; i * i <= n; i++) if(n % i == 0)
        {
            prime = 0;
            break;
        }
        if(prime) printf("%d ", n);
    }
    putchar('\n');
    return 0;
}
```
<!-- reference-c:end -->

</details>
