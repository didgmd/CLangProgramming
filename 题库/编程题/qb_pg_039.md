<!-- question-meta
id: QB-PG-039
category: 编程题
chapters: 5
concepts: 二分查找、整数溢出
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 非负整数平方根整数部分

## 题目



输入非负整数，用二分查找输出平方根的整数部分。

### 输入格式

一个非负整数 `n`。

### 输出格式

输出 `sqrt(n)` 的整数部分。

### 数据范围与边界

输入必须非负，计算过程中避免整数乘法溢出。

### 样例输入

```text
20
```

### 样例输出

```text
4
```

## 常见失分点



围绕“非负整数平方根整数部分”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 在满足 `k*k<=n` 的范围内寻找最大整数 `k`。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `0`；完全平方数；相邻平方数之间的数。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    unsigned n;
    if(scanf("%u", & n) != 1) return 1;
    unsigned lo = 0, hi = n < 65535 ? n : 65535, ans = 0;
    while(lo <= hi)
    {
        unsigned mid = lo + (hi - lo) / 2;
        if(mid == 0 || mid <= n / mid)
        {
            ans = mid;
            lo = mid + 1;
        }
        else hi = mid - 1;
    }
    printf("%u\n", ans);
    return 0;
}
```
<!-- reference-c:end -->

</details>
