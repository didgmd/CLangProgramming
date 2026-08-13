# 上机课

共8次上机课、16学时。每次2课时、90分钟，在无网络、无手机条件下使用VS Code和MinGW GCC独立完成1道考试型编程题。

学生在上机过程中完成程序编写、运行、调试和结果记录，并将过程与结果填写到教师发放的实验报告模板。完成后的实验报告保存为PDF格式并提交至超星学习通；程序源码和运行产物不属于提交材料。

| ID | 已学章节 | 实验项目 | 题目ID | 状态 |
|---|---|---|---|---|
| [CW-LAB01](01-day-of-year/README.md) | 第1–4章 | 日期序号计算 | `QB-PG-005` | ready |
| [CW-LAB02](02-character-count/README.md) | 第1–5章 | 四类字符统计 | `QB-PG-019` | ready |
| [CW-LAB03](03-word-count/README.md) | 第1–5章 | 单词数量统计 | `QB-PG-012` | ready |
| [CW-LAB04](04-matrix-transpose/README.md) | 第1–6章 | 三阶矩阵转置 | `QB-PG-021` | ready |
| [CW-LAB05](05-string-to-integer/README.md) | 第1–6章 | 数字字符串转换 | `QB-PG-007` | ready |
| [CW-LAB06](06-pascal-triangle/README.md) | 第1–6章 | 杨辉三角 | `QB-PG-020` | ready |
| [CW-LAB07](07-scenic-sort/README.md) | 第1–6章 | 景点距离排序 | `QB-PG-016` | ready |
| [CW-LAB08](08-file-score-statistics/README.md) | 第1–10章 | 成绩文件统计 | `QB-PG-042` | ready |

## 正式任务单接口

每份任务单依次包含实验项目、实验目的、实验步骤、打印分页和参考完整程序。测试情形及预期结果直接纳入实验步骤。参考程序的严格编译和行为测试属于仓库维护校验，不作为学生任务单章节。

执行下列命令验证全部任务单：

```powershell
conda run -n base python tools/validate_labs.py
```
