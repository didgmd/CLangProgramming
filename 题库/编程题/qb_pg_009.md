<!-- question-meta
id: QB-PG-009
category: 编程题
chapters: 5
concepts: 素数、嵌套循环
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 区间素数

## 题目




输出100到200之间的全部素数，每行最多输出5个。

### 输入格式

无输入。

### 输出格式

按升序输出100到200之间的素数，每行5个，最后一行可以不足5个。

### 数据范围与边界

候选整数固定为闭区间 `[100, 200]`。

### 样例输入

```text
（无输入）
```

### 样例输出

```text
101 103 107 109 113
127 131 137 139 149
151 157 163 167 173
179 181 191 193 197
199
```

## 常见失分点

- 候选范围必须是闭区间 `[100, 200]`。
- 每检查一个新的候选数，都要把素数标志重新设为1。
- 内层试除只需进行到平方根附近，条件可写为 `i <= n / i`。
- 找到因数后，`break`只结束当前试除循环，外层循环仍继续检查下一个候选数。
- 输出计数应在输出素数后更新，并保证每行最多5个。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 外层循环逐个产生100至200的候选数；每个候选数开始时重置素数标志，内层循环进行试除。找到因数后将标志改为0并结束内层循环；标志仍为1时输出该素数，并用计数器控制每行5个。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** 核对首个结果为101、末个结果为199，并检查每行数量。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>

int main()
{
    int n, i;
    int is_prime;
    int count = 0;

    for (n = 100; n <= 200; n++)
    {
        is_prime = 1;

        for (i = 2; i <= n / i; i++)
        {
            if (n % i == 0)
            {
                is_prime = 0;
                break;
            }
        }

        if (is_prime)
        {
            if (count % 5 != 0)
            {
                printf(" ");
            }

            printf("%d", n);
            count++;

            if (count % 5 == 0)
            {
                printf("\n");
            }
        }
    }

    if (count % 5 != 0)
    {
        printf("\n");
    }

    return 0;
}
```
<!-- reference-c:end -->

</details>
