<!-- question-meta
id: QB-PG-014
category: 编程题
chapters: 5
concepts: 数位分解
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 四位数各位立方和

## 题目



输入四位正整数，求各位数字立方和。

### 输入格式

一个四位正整数。

### 输出格式

输出四个数位的立方和。

### 数据范围与边界

输入范围1000至9999。

### 样例输入

```text
1234
```

### 样例输出

```text
100
```

## 常见失分点



围绕“四位数各位立方和”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 反复使用除10和模10分离数位。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `1000`；`9999`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int n;
    if(scanf("%d", & n) != 1 || n < 1000 || n > 9999)
    {
        puts("invalid");
        return 0;
    }
    int sum = 0;
    for(int x = n; x; x /= 10)
    {
        int d = x % 10;
        sum += d * d * d;
    }
    printf("%d\n", sum);
    return 0;
}
```
<!-- reference-c:end -->

</details>
