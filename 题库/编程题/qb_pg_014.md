<!-- question-meta
id: QB-PG-014
category: 编程题
chapters: 3
concepts: 顺序结构、整数除法、取余、数位分解
difficulty: 常规
minutes: 15
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



不要使用 `^` 表示乘方；C语言中的 `^` 是按位异或运算符。提取百位和十位时，注意先用整数除法去掉低位，再用 `% 10` 保留当前数位。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 使用整数除法和取余分别得到千位、百位、十位和个位，再把四个数位的立方相加。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `1234`得到`100`；`1000`得到`1`；`9999`得到`2916`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main()
{
    int n;
    int thousands, hundreds, tens, ones;
    int sum;

    scanf("%d", &n);

    thousands = n / 1000;
    hundreds = n / 100 % 10;
    tens = n / 10 % 10;
    ones = n % 10;

    sum = thousands * thousands * thousands;
    sum = sum + hundreds * hundreds * hundreds;
    sum = sum + tens * tens * tens;
    sum = sum + ones * ones * ones;

    printf("%d\n", sum);

    return 0;
}
```
<!-- reference-c:end -->

</details>
