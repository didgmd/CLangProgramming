<!-- question-meta
id: QB-PG-036
category: 编程题
chapters: 6
concepts: 杨辉三角、边界
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 可变行数杨辉三角

## 题目



输入1到20之间的行数，输出杨辉三角。

### 输入格式

一个整数 `n`。

### 输出格式

输出杨辉三角前 `n` 行，每行元素以空格分隔。

### 数据范围与边界

行数不得超过参考程序二维数组的容量。

### 样例输入

```text
4
```

### 样例输出

```text
1
1 1
1 2 1
1 3 3 1
```

## 常见失分点



围绕“可变行数杨辉三角”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 先设每行两端为1，再用上一行相邻两项计算内部元素。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `n=1`（最小行数）；`n=4`（包含内部递推）。

### 完整参考程序

<!-- reference-c:start -->
```c
#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
int main(void)
{
    int n;
    if(scanf("%d", & n) != 1 || n < 1 || n > 20) return 1;
    long long a [20] [20] =
    {
        {
            0
        }
    }
    ;
    for(int i = 0; i < n; i++)
    {
        a [i] [0] = a [i] [i] = 1;
        for(int j = 1; j < i; j++) a [i] [j] = a [i - 1] [j - 1] + a [i - 1] [j];
        for(int j = 0; j <= i; j++) printf("%lld%c", a [i] [j], j == i ? '\n' : ' ');
    }
    return 0;
}
```
<!-- reference-c:end -->

</details>
