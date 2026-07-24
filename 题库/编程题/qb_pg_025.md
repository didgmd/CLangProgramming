<!-- question-meta
id: QB-PG-025
category: 编程题
chapters: 4、6
concepts: 日期、闰年
difficulty: 综合
minutes: 20
related_routines: 无
compile_mode: c11-strict
legacy_features: 无
-->
# 日期合法性与序号

## 题目



输入年月日，先验证日期，再计算当年第几天。

### 输入格式

三个整数 `year month day`。

### 输出格式

合法时输出年内序号，非法时输出 `invalid`。

### 数据范围与边界

月份为1至12，日必须落在该月实际天数内。

### 样例输入

```text
2024 2 29
```

### 样例输出

```text
60
```

## 常见失分点



围绕“日期合法性与序号”检查输入合法性、临界值、数组或循环边界，并严格匹配题目规定的输出格式。

<details>
<summary>参考答案与解析</summary>

**解题思路：** 先修正闰年二月天数，再校验并累加此前月份。

**评分建议：** 输入与边界处理2分，核心算法5分，正确输出2分，代码规范1分。

**正常与边界测试：** `2024 2 29`；`2023 2 29`。

### 完整参考程序

<!-- reference-c:start -->
```c
#include <stdio.h>
int main(void)
{
    int y, m, d;
    if (scanf("%d%d%d", &y, &m, &d) != 3)
    {
        return 1;
    }
    int days[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0))
    {
        days[2] = 29;
    }
    if (m < 1 || m > 12 || d < 1 || d > days[m])
    {
        puts("invalid");
        return 0;
    }
    int sum = d;
    for (int i = 1; i < m; i++)
    {
        sum += days[i];
    }
    printf("%d\n", sum);
    return 0;
}
```
<!-- reference-c:end -->

</details>
