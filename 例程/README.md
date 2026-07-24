# C 语言例程库

本目录以谭浩强《C程序设计（第五版）》第 1–10 章为主轴，仅支持 MinGW-w64 GCC。例程元数据以源码文件头为准。

当前共 195 个例程：104 个 `c11-strict`，91 个 `gnu99-textbook`。

源码头中的 `来源` 字段保留历史 provenance；旧学期路径不再是工作区目录，需通过 Git 历史恢复原始文件。

## 最短使用路径

```powershell
# 验证全部例程
conda run -n base python tools/validate_routines.py

# 验证单个例程（多文件例程会自动整体构建）
conda run -n base python tools/validate_routines.py --id EX-C05-010

# 检查本索引是否与源码头一致
conda run -n base python tools/generate_routine_index.py --check
```

单文件例程也可在仓库根目录直接编译，例如：

```powershell
gcc -std=c11 -Wall -Wextra -Wpedantic -Werror "例程/chapters/01-programming-and-c/ex_c01_001_1_1.c" -o hello.exe
.\hello.exe
Remove-Item -LiteralPath .\hello.exe
```

`gets()`、`conio.h` 等教材旧接口的适用边界写在对应源码文件头。

## 第 1 章 程序设计和 C 语言

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C01-001 | 教材例程 1.1 | 第 1 章 / 1.1 | 程序结构、编译与运行、基本输出 | c11-strict | 无 | [`ex_c01_001_1_1.c`](chapters/01-programming-and-c/ex_c01_001_1_1.c) |
| EX-C01-002 | 教材例程 1.2 | 第 1 章 / 1.2 | 程序结构、编译与运行、基本输出 | c11-strict | 无 | [`ex_c01_002_1_2.c`](chapters/01-programming-and-c/ex_c01_002_1_2.c) |
| EX-C01-003 | 教材例程 1.2.1 | 第 1 章 / 1.2.1 | 程序结构、编译与运行、基本输出 | c11-strict | 无 | [`ex_c01_003_1_2_1_add.c`](chapters/01-programming-and-c/ex_c01_003_1_2_1_add.c) |
| EX-C01-004 | 教材例程 1.2.2 | 第 1 章 / 1.2.2 | 程序结构、编译与运行、基本输出 | c11-strict | 无 | [`ex_c01_004_1_2_2_addtwonumbers.c`](chapters/01-programming-and-c/ex_c01_004_1_2_2_addtwonumbers.c) |
| EX-C01-005 | 教材例程 1.3 | 第 1 章 / 1.3 | 程序结构、编译与运行、基本输出 | gnu99-textbook | 无 | [`ex_c01_005_1_3.c`](chapters/01-programming-and-c/ex_c01_005_1_3.c) |
| EX-C01-006 | 教材例程 1.5.1 | 第 1 章 / 1.5.1 | 程序结构、编译与运行、基本输出 | c11-strict | 无 | [`ex_c01_006_1_5_1_forloop.c`](chapters/01-programming-and-c/ex_c01_006_1_5_1_forloop.c) |
| EX-C01-007 | 教材例程 1.5.3 | 第 1 章 / 1.5.3 | 程序结构、编译与运行、基本输出 | c11-strict | 无 | [`ex_c01_007_1_5_3_whileloop.c`](chapters/01-programming-and-c/ex_c01_007_1_5_3_whileloop.c) |

## 第 2 章 算法——程序的灵魂

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C02-001 | 教材例程 2.1.1 | 第 2 章 / 2.1.1 | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_001_ex2_1_1.c`](chapters/02-algorithms/ex_c02_001_ex2_1_1.c) |
| EX-C02-002 | 教材例程 2.1.2 | 第 2 章 / 2.1.2 | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_002_ex2_1_2.c`](chapters/02-algorithms/ex_c02_002_ex2_1_2.c) |
| EX-C02-003 | 教材例程 2.1_2.6 | 第 2 章 / 2.1_2.6 | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_003_2_1_2_6.c`](chapters/02-algorithms/ex_c02_003_2_1_2_6.c) |
| EX-C02-004 | 教材例程 2.2 | 第 2 章 / 2.2 | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_004_ex2_2.c`](chapters/02-algorithms/ex_c02_004_ex2_2.c) |
| EX-C02-005 | 教材例程 2.2_2.7 | 第 2 章 / 2.2_2.7 | 算法、流程控制、问题求解 | gnu99-textbook | 无 | [`ex_c02_005_2_2_2_7.c`](chapters/02-algorithms/ex_c02_005_2_2_2_7.c) |
| EX-C02-006 | 教材例程 2.3 | 第 2 章 / 2.3 | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_006_ex2_3.c`](chapters/02-algorithms/ex_c02_006_ex2_3.c) |
| EX-C02-007 | 教材例程 2.3_2.8 | 第 2 章 / 2.3_2.8 | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_007_2_3_2_8.c`](chapters/02-algorithms/ex_c02_007_2_3_2_8.c) |
| EX-C02-008 | 教材例程 2.4 | 第 2 章 / 2.4 | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_008_ex2_4.c`](chapters/02-algorithms/ex_c02_008_ex2_4.c) |
| EX-C02-009 | 教材例程 2.4-class | 第 2 章 / 2.4-class | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_009_ex2_4.c`](chapters/02-algorithms/ex_c02_009_ex2_4.c) |
| EX-C02-010 | 教材例程 2.4_2.9 | 第 2 章 / 2.4_2.9 | 算法、流程控制、问题求解 | c11-strict | 无 | [`ex_c02_010_2_4_2_9.c`](chapters/02-algorithms/ex_c02_010_2_4_2_9.c) |
| EX-C02-011 | 教材例程 2.5 | 第 2 章 / 2.5 | 算法、流程控制、问题求解 | gnu99-textbook | 无 | [`ex_c02_011_ex2_5.c`](chapters/02-algorithms/ex_c02_011_ex2_5.c) |
| EX-C02-012 | 教材例程 2.5_2.10 | 第 2 章 / 2.5_2.10 | 算法、流程控制、问题求解 | gnu99-textbook | 无 | [`ex_c02_012_2_5_2_10.c`](chapters/02-algorithms/ex_c02_012_2_5_2_10.c) |

## 第 3 章 顺序程序设计

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C03-001 | 教材例程 3.1 | 第 3 章 / 3.1 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_001_3_1.c`](chapters/03-sequential-programming/ex_c03_001_3_1.c) |
| EX-C03-002 | 教材例程 3.2 | 第 3 章 / 3.2 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_002_3_2.c`](chapters/03-sequential-programming/ex_c03_002_3_2.c) |
| EX-C03-003 | 教材例程 3.3 | 第 3 章 / 3.3 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_003_3_3.c`](chapters/03-sequential-programming/ex_c03_003_3_3.c) |
| EX-C03-004 | 教材例程 3.4 | 第 3 章 / 3.4 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_004_3_4.c`](chapters/03-sequential-programming/ex_c03_004_3_4.c) |
| EX-C03-005 | 教材例程 3.5 | 第 3 章 / 3.5 | 数据类型、运算符、输入输出 | gnu99-textbook | 无 | [`ex_c03_005_3_5.c`](chapters/03-sequential-programming/ex_c03_005_3_5.c) |
| EX-C03-006 | 教材例程 3.6 | 第 3 章 / 3.6 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_006_12_ex3_6.c`](chapters/03-sequential-programming/ex_c03_006_12_ex3_6.c) |
| EX-C03-007 | 教材例程 3.6.1 | 第 3 章 / 3.6.1 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_007_3_6_1.c`](chapters/03-sequential-programming/ex_c03_007_3_6_1.c) |
| EX-C03-008 | 教材例程 3.6.2 | 第 3 章 / 3.6.2 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_008_3_6_2.c`](chapters/03-sequential-programming/ex_c03_008_3_6_2.c) |
| EX-C03-009 | 教材例程 3.8 | 第 3 章 / 3.8 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_009_13_ex3_8.c`](chapters/03-sequential-programming/ex_c03_009_13_ex3_8.c) |
| EX-C03-010 | 教材例程 3.8.1 | 第 3 章 / 3.8.1 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_010_3_8_1.c`](chapters/03-sequential-programming/ex_c03_010_3_8_1.c) |
| EX-C03-011 | 教材例程 3.8.2 | 第 3 章 / 3.8.2 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_011_3_8_2.c`](chapters/03-sequential-programming/ex_c03_011_3_8_2.c) |
| EX-C03-012 | 教材例程 3.9 | 第 3 章 / 3.9 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_012_3_9.c`](chapters/03-sequential-programming/ex_c03_012_3_9.c) |
| EX-C03-013 | 教材例程 3.10 | 第 3 章 / 3.10 | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_013_3_10.c`](chapters/03-sequential-programming/ex_c03_013_3_10.c) |
| EX-C03-014 | 教材例程 custom-01_floatdouble | 第 3 章 / custom-01_floatdouble | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_014_01_floatdouble.c`](chapters/03-sequential-programming/ex_c03_014_01_floatdouble.c) |
| EX-C03-015 | 教材例程 custom-02_decocthex | 第 3 章 / custom-02_decocthex | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_015_02_decocthex.c`](chapters/03-sequential-programming/ex_c03_015_02_decocthex.c) |
| EX-C03-016 | 教材例程 custom-03_integer | 第 3 章 / custom-03_integer | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_016_03_integer.c`](chapters/03-sequential-programming/ex_c03_016_03_integer.c) |
| EX-C03-017 | 教材例程 custom-04_complement | 第 3 章 / custom-04_complement | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_017_04_complement.c`](chapters/03-sequential-programming/ex_c03_017_04_complement.c) |
| EX-C03-018 | 教材例程 custom-05_selfoperation | 第 3 章 / custom-05_selfoperation | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_018_05_selfoperation.c`](chapters/03-sequential-programming/ex_c03_018_05_selfoperation.c) |
| EX-C03-019 | 教材例程 custom-08_switch | 第 3 章 / custom-08_switch | 数据类型、运算符、输入输出 | gnu99-textbook | msvc-crt-compat | [`ex_c03_019_08_switch.c`](chapters/03-sequential-programming/ex_c03_019_08_switch.c) |
| EX-C03-020 | 教材例程 custom-09_alignment | 第 3 章 / custom-09_alignment | 数据类型、运算符、输入输出 | c11-strict | 无 | [`ex_c03_020_09_alignment.c`](chapters/03-sequential-programming/ex_c03_020_09_alignment.c) |

## 第 4 章 选择结构程序设计

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C04-001 | 教材例程 4.1 | 第 4 章 / 4.1 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_001_4_1.c`](chapters/04-selection/ex_c04_001_4_1.c) |
| EX-C04-002 | 教材例程 4.2 | 第 4 章 / 4.2 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_002_4_2.c`](chapters/04-selection/ex_c04_002_4_2.c) |
| EX-C04-003 | 教材例程 4.3 | 第 4 章 / 4.3 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_003_4_3.c`](chapters/04-selection/ex_c04_003_4_3.c) |
| EX-C04-004 | 教材例程 4.4 | 第 4 章 / 4.4 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_004_4_4.c`](chapters/04-selection/ex_c04_004_4_4.c) |
| EX-C04-005 | 教材例程 4.5 | 第 4 章 / 4.5 | if、switch、条件表达式 | gnu99-textbook | msvc-crt-compat | [`ex_c04_005_ex_4_05.c`](chapters/04-selection/ex_c04_005_ex_4_05.c) |
| EX-C04-006 | 教材例程 4.5.1 | 第 4 章 / 4.5.1 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_006_4_5_1.c`](chapters/04-selection/ex_c04_006_4_5_1.c) |
| EX-C04-007 | 教材例程 4.5.2 | 第 4 章 / 4.5.2 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_007_4_5_2.c`](chapters/04-selection/ex_c04_007_4_5_2.c) |
| EX-C04-008 | 教材例程 4.6 | 第 4 章 / 4.6 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_008_4_6.c`](chapters/04-selection/ex_c04_008_4_6.c) |
| EX-C04-009 | 教材例程 4.7 | 第 4 章 / 4.7 | if、switch、条件表达式 | c11-strict | 无 | [`ex_c04_009_4_7.c`](chapters/04-selection/ex_c04_009_4_7.c) |
| EX-C04-010 | 教材例程 4.8 | 第 4 章 / 4.8 | if、switch、条件表达式 | gnu99-textbook | msvc-crt-compat | [`ex_c04_010_ex_4_08.c`](chapters/04-selection/ex_c04_010_ex_4_08.c) |
| EX-C04-011 | 教材例程 4.8.1 | 第 4 章 / 4.8.1 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_011_4_8_1.c`](chapters/04-selection/ex_c04_011_4_8_1.c) |
| EX-C04-012 | 教材例程 4.8.2 | 第 4 章 / 4.8.2 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_012_4_8_2.c`](chapters/04-selection/ex_c04_012_4_8_2.c) |
| EX-C04-013 | 教材例程 4.8.3 | 第 4 章 / 4.8.3 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_013_4_8_3.c`](chapters/04-selection/ex_c04_013_4_8_3.c) |
| EX-C04-014 | 教材例程 4.9 | 第 4 章 / 4.9 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_014_4_9.c`](chapters/04-selection/ex_c04_014_4_9.c) |
| EX-C04-015 | 教材例程 4.10 | 第 4 章 / 4.10 | if、switch、条件表达式 | gnu99-textbook | 无 | [`ex_c04_015_4_10.c`](chapters/04-selection/ex_c04_015_4_10.c) |

## 第 5 章 循环结构程序设计

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C05-001 | 教材例程 5.1 | 第 5 章 / 5.1 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_001_5_1.c`](chapters/05-loops/ex_c05_001_5_1.c) |
| EX-C05-002 | 教材例程 5.2 | 第 5 章 / 5.2 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_002_5_2.c`](chapters/05-loops/ex_c05_002_5_2.c) |
| EX-C05-003 | 教材例程 5.3.1 | 第 5 章 / 5.3.1 | while、do-while、for、break、continue | gnu99-textbook | 无 | [`ex_c05_003_5_3_1.c`](chapters/05-loops/ex_c05_003_5_3_1.c) |
| EX-C05-004 | 教材例程 5.3.2 | 第 5 章 / 5.3.2 | while、do-while、for、break、continue | gnu99-textbook | 无 | [`ex_c05_004_5_3_2.c`](chapters/05-loops/ex_c05_004_5_3_2.c) |
| EX-C05-005 | 教材例程 5.4 | 第 5 章 / 5.4 | while、do-while、for、break、continue | gnu99-textbook | 无 | [`ex_c05_005_5_4.c`](chapters/05-loops/ex_c05_005_5_4.c) |
| EX-C05-006 | 教材例程 5.5 | 第 5 章 / 5.5 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_006_5_5.c`](chapters/05-loops/ex_c05_006_5_5.c) |
| EX-C05-007 | 教材例程 5.6 | 第 5 章 / 5.6 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_007_5_6.c`](chapters/05-loops/ex_c05_007_5_6.c) |
| EX-C05-008 | 教材例程 5.7 | 第 5 章 / 5.7 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_008_5_7.c`](chapters/05-loops/ex_c05_008_5_7.c) |
| EX-C05-009 | 教材例程 5.8.1 | 第 5 章 / 5.8.1 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_009_5_8_1.c`](chapters/05-loops/ex_c05_009_5_8_1.c) |
| EX-C05-010 | 教材例程 5.8.2 | 第 5 章 / 5.8.2 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_010_5_8_2.c`](chapters/05-loops/ex_c05_010_5_8_2.c) |
| EX-C05-011 | 教材例程 5.9.1 | 第 5 章 / 5.9.1 | while、do-while、for、break、continue | gnu99-textbook | 无 | [`ex_c05_011_5_9_1.c`](chapters/05-loops/ex_c05_011_5_9_1.c) |
| EX-C05-012 | 教材例程 5.9.2 | 第 5 章 / 5.9.2 | while、do-while、for、break、continue | gnu99-textbook | 无 | [`ex_c05_012_5_9_2.c`](chapters/05-loops/ex_c05_012_5_9_2.c) |
| EX-C05-013 | 教材例程 5.10 | 第 5 章 / 5.10 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_013_5_10.c`](chapters/05-loops/ex_c05_013_5_10.c) |
| EX-C05-014 | 教材例程 5.11 | 第 5 章 / 5.11 | while、do-while、for、break、continue | c11-strict | 无 | [`ex_c05_014_5_11.c`](chapters/05-loops/ex_c05_014_5_11.c) |

## 第 6 章 利用数组处理批量数据

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C06-001 | 教材例程 6.1 | 第 6 章 / 6.1 | 一维数组、二维数组、字符数组、字符串 | c11-strict | 无 | [`ex_c06_001_6_1.c`](chapters/06-arrays-and-strings/ex_c06_001_6_1.c) |
| EX-C06-002 | 教材例程 6.2 | 第 6 章 / 6.2 | 一维数组、二维数组、字符数组、字符串 | c11-strict | 无 | [`ex_c06_002_6_2.c`](chapters/06-arrays-and-strings/ex_c06_002_6_2.c) |
| EX-C06-003 | 教材例程 6.3 | 第 6 章 / 6.3 | 一维数组、二维数组、字符数组、字符串 | gnu99-textbook | 无 | [`ex_c06_003_6_3.c`](chapters/06-arrays-and-strings/ex_c06_003_6_3.c) |
| EX-C06-004 | 教材例程 6.4 | 第 6 章 / 6.4 | 一维数组、二维数组、字符数组、字符串 | c11-strict | 无 | [`ex_c06_004_6_4.c`](chapters/06-arrays-and-strings/ex_c06_004_6_4.c) |
| EX-C06-005 | 教材例程 6.5 | 第 6 章 / 6.5 | 一维数组、二维数组、字符数组、字符串 | c11-strict | 无 | [`ex_c06_005_6_5.c`](chapters/06-arrays-and-strings/ex_c06_005_6_5.c) |
| EX-C06-006 | 教材例程 6.6 | 第 6 章 / 6.6 | 一维数组、二维数组、字符数组、字符串 | c11-strict | 无 | [`ex_c06_006_6_6.c`](chapters/06-arrays-and-strings/ex_c06_006_6_6.c) |
| EX-C06-007 | 教材例程 6.7 | 第 6 章 / 6.7 | 一维数组、二维数组、字符数组、字符串 | c11-strict | 无 | [`ex_c06_007_6_7.c`](chapters/06-arrays-and-strings/ex_c06_007_6_7.c) |
| EX-C06-008 | 教材例程 6.8 | 第 6 章 / 6.8 | 一维数组、二维数组、字符数组、字符串 | gnu99-textbook | gets | [`ex_c06_008_6_8.c`](chapters/06-arrays-and-strings/ex_c06_008_6_8.c) |
| EX-C06-009 | 教材例程 6.9 | 第 6 章 / 6.9 | 一维数组、二维数组、字符数组、字符串 | gnu99-textbook | gets | [`ex_c06_009_6_9.c`](chapters/06-arrays-and-strings/ex_c06_009_6_9.c) |
| EX-C06-010 | 教材例程 custom-06_pointer | 第 6 章 / custom-06_pointer | 一维数组、二维数组、字符数组、字符串 | c11-strict | 无 | [`ex_c06_010_06_pointer.c`](chapters/06-arrays-and-strings/ex_c06_010_06_pointer.c) |
| EX-C06-011 | 教材例程 custom-09_diamondspause | 第 6 章 / custom-09_diamondspause | 一维数组、二维数组、字符数组、字符串 | gnu99-textbook | system-pause | [`ex_c06_011_09_diamondspause.c`](chapters/06-arrays-and-strings/ex_c06_011_09_diamondspause.c) |
| EX-C06-012 | 教材例程 custom-10_string | 第 6 章 / custom-10_string | 一维数组、二维数组、字符数组、字符串 | c11-strict | 无 | [`ex_c06_012_10_string.c`](chapters/06-arrays-and-strings/ex_c06_012_10_string.c) |
| EX-C06-013 | 教材例程 custom-12_strcat | 第 6 章 / custom-12_strcat | 一维数组、二维数组、字符数组、字符串 | gnu99-textbook | msvc-crt-compat | [`ex_c06_013_12_strcat.c`](chapters/06-arrays-and-strings/ex_c06_013_12_strcat.c) |

## 第 7 章 用函数实现模块化程序设计

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C07-001 | 教材例程 7.1 | 第 7 章 / 7.1 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_001_7_1.c`](chapters/07-functions/ex_c07_001_7_1.c) |
| EX-C07-002 | 教材例程 7.2 | 第 7 章 / 7.2 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_002_7_2.c`](chapters/07-functions/ex_c07_002_7_2.c) |
| EX-C07-003 | 教材例程 7.3 | 第 7 章 / 7.3 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_003_7_3.c`](chapters/07-functions/ex_c07_003_7_3.c) |
| EX-C07-004 | 教材例程 7.4 | 第 7 章 / 7.4 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_004_7_4.c`](chapters/07-functions/ex_c07_004_7_4.c) |
| EX-C07-005 | 教材例程 7.5 | 第 7 章 / 7.5 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_005_7_5.c`](chapters/07-functions/ex_c07_005_7_5.c) |
| EX-C07-006 | 教材例程 7.6 | 第 7 章 / 7.6 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_006_7_6.c`](chapters/07-functions/ex_c07_006_7_6.c) |
| EX-C07-007 | 教材例程 7.7 | 第 7 章 / 7.7 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_007_7_7.c`](chapters/07-functions/ex_c07_007_7_7.c) |
| EX-C07-008 | 教材例程 7.8 | 第 7 章 / 7.8 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_008_7_8.c`](chapters/07-functions/ex_c07_008_7_8.c) |
| EX-C07-009 | 教材例程 7.9 | 第 7 章 / 7.9 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_009_7_9.c`](chapters/07-functions/ex_c07_009_7_9.c) |
| EX-C07-010 | 教材例程 7.10 | 第 7 章 / 7.10 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_010_7_10.c`](chapters/07-functions/ex_c07_010_7_10.c) |
| EX-C07-011 | 教材例程 7.11 | 第 7 章 / 7.11 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_011_7_11.c`](chapters/07-functions/ex_c07_011_7_11.c) |
| EX-C07-012 | 教材例程 7.12 | 第 7 章 / 7.12 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_012_7_12.c`](chapters/07-functions/ex_c07_012_7_12.c) |
| EX-C07-013 | 教材例程 7.13 | 第 7 章 / 7.13 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_013_7_13.c`](chapters/07-functions/ex_c07_013_7_13.c) |
| EX-C07-014 | 教材例程 7.14 | 第 7 章 / 7.14 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_014_7_14.c`](chapters/07-functions/ex_c07_014_7_14.c) |
| EX-C07-015 | 教材例程 7.15 | 第 7 章 / 7.15 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_015_7_15.c`](chapters/07-functions/ex_c07_015_7_15.c) |
| EX-C07-016 | 教材例程 7.16 | 第 7 章 / 7.16 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_016_7_16.c`](chapters/07-functions/ex_c07_016_7_16.c) |
| EX-C07-017 | 教材例程 7.17 | 第 7 章 / 7.17 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_017_7_17.c`](chapters/07-functions/ex_c07_017_7_17.c) |
| EX-C07-018 | 教材例程 7.18 | 第 7 章 / 7.18 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`ex_c07_018_7_18.c`](chapters/07-functions/ex_c07_018_7_18.c) |
| EX-C07-019 | 教材例程 7.19 | 第 7 章 / 7.19 | 函数、参数、递归、变量作用域 | gnu99-textbook | 无 | [`source_01.c`](chapters/07-functions/ex_c07_019/source_01.c)<br>[`source_02.c`](chapters/07-functions/ex_c07_019/source_02.c) |
| EX-C07-020 | 教材例程 7.20 | 第 7 章 / 7.20 | 函数、参数、递归、变量作用域 | gnu99-textbook | gets | [`source_01.c`](chapters/07-functions/ex_c07_020/source_01.c)<br>[`source_02.c`](chapters/07-functions/ex_c07_020/source_02.c)<br>[`source_03.c`](chapters/07-functions/ex_c07_020/source_03.c)<br>[`source_04.c`](chapters/07-functions/ex_c07_020/source_04.c) |
| EX-C07-021 | 实验演示 lab5.4 | 第 7 章 / lab5.4 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_021_04.c`](chapters/07-functions/ex_c07_021_04.c) |
| EX-C07-022 | 实验演示 lab5.10 | 第 7 章 / lab5.10 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_022_10.c`](chapters/07-functions/ex_c07_022_10.c) |
| EX-C07-023 | 实验演示 lab5.11 | 第 7 章 / lab5.11 | 函数、参数、递归、变量作用域 | c11-strict | 无 | [`ex_c07_023_11.c`](chapters/07-functions/ex_c07_023_11.c) |

## 第 8 章 善于利用指针

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C08-001 | 教材例程 8.1 | 第 8 章 / 8.1 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_001_8_1.c`](chapters/08-pointers/ex_c08_001_8_1.c) |
| EX-C08-002 | 教材例程 8.2 | 第 8 章 / 8.2 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_002_8_2.c`](chapters/08-pointers/ex_c08_002_8_2.c) |
| EX-C08-003 | 教材例程 8.3 | 第 8 章 / 8.3 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_003_8_3.c`](chapters/08-pointers/ex_c08_003_8_3.c) |
| EX-C08-004 | 教材例程 8.4 | 第 8 章 / 8.4 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_004_8_4.c`](chapters/08-pointers/ex_c08_004_8_4.c) |
| EX-C08-005 | 教材例程 8.5 | 第 8 章 / 8.5 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_005_8_5.c`](chapters/08-pointers/ex_c08_005_8_5.c) |
| EX-C08-006 | 教材例程 8.6.1 | 第 8 章 / 8.6.1 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_006_8_6_1.c`](chapters/08-pointers/ex_c08_006_8_6_1.c) |
| EX-C08-007 | 教材例程 8.6.2 | 第 8 章 / 8.6.2 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_007_8_6_2.c`](chapters/08-pointers/ex_c08_007_8_6_2.c) |
| EX-C08-008 | 教材例程 8.6.3 | 第 8 章 / 8.6.3 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_008_8_6_3.c`](chapters/08-pointers/ex_c08_008_8_6_3.c) |
| EX-C08-009 | 教材例程 8.7.1 | 第 8 章 / 8.7.1 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_009_8_7_1.c`](chapters/08-pointers/ex_c08_009_8_7_1.c) |
| EX-C08-010 | 教材例程 8.7.2 | 第 8 章 / 8.7.2 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_010_8_7_2.c`](chapters/08-pointers/ex_c08_010_8_7_2.c) |
| EX-C08-011 | 教材例程 8.8.1 | 第 8 章 / 8.8.1 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_011_8_8_1.c`](chapters/08-pointers/ex_c08_011_8_8_1.c) |
| EX-C08-012 | 教材例程 8.8.2 | 第 8 章 / 8.8.2 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_012_8_8_2.c`](chapters/08-pointers/ex_c08_012_8_8_2.c) |
| EX-C08-013 | 教材例程 8.9.1 | 第 8 章 / 8.9.1 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_013_8_9_1.c`](chapters/08-pointers/ex_c08_013_8_9_1.c) |
| EX-C08-014 | 教材例程 8.10.1 | 第 8 章 / 8.10.1 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_014_8_10_1.c`](chapters/08-pointers/ex_c08_014_8_10_1.c) |
| EX-C08-015 | 教材例程 8.10.2 | 第 8 章 / 8.10.2 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | 无 | [`ex_c08_015_8_10_2.c`](chapters/08-pointers/ex_c08_015_8_10_2.c) |
| EX-C08-016 | 教材例程 8.11 | 第 8 章 / 8.11 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_016_19_ex_8_11.c`](chapters/08-pointers/ex_c08_016_19_ex_8_11.c) |
| EX-C08-017 | 教材例程 8.12 | 第 8 章 / 8.12 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_017_20_ex_8_12.c`](chapters/08-pointers/ex_c08_017_20_ex_8_12.c) |
| EX-C08-018 | 教材例程 8.13.1 | 第 8 章 / 8.13.1 | 指针、数组与指针、字符串指针、动态内存 | gnu99-textbook | msvc-crt-compat | [`ex_c08_018_21_ex_8_13_1.c`](chapters/08-pointers/ex_c08_018_21_ex_8_13_1.c) |
| EX-C08-019 | 教材例程 8.13.2 | 第 8 章 / 8.13.2 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_019_22_ex_8_13_2.c`](chapters/08-pointers/ex_c08_019_22_ex_8_13_2.c) |
| EX-C08-020 | 教材例程 8.14 | 第 8 章 / 8.14 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_020_23_ex_8_14.c`](chapters/08-pointers/ex_c08_020_23_ex_8_14.c) |
| EX-C08-021 | 教材例程 8.15 | 第 8 章 / 8.15 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_021_24_ex_8_15.c`](chapters/08-pointers/ex_c08_021_24_ex_8_15.c) |
| EX-C08-022 | 教材例程 8.16 | 第 8 章 / 8.16 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_022_8_16.c`](chapters/08-pointers/ex_c08_022_8_16.c) |
| EX-C08-023 | 教材例程 8.17 | 第 8 章 / 8.17 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_023_8_17.c`](chapters/08-pointers/ex_c08_023_8_17.c) |
| EX-C08-024 | 教材例程 8.18 | 第 8 章 / 8.18 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_024_8_18.c`](chapters/08-pointers/ex_c08_024_8_18.c) |
| EX-C08-025 | 教材例程 8.19 | 第 8 章 / 8.19 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_025_8_19.c`](chapters/08-pointers/ex_c08_025_8_19.c) |
| EX-C08-026 | 教材例程 8.20.1 | 第 8 章 / 8.20.1 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_026_8_20_1.c`](chapters/08-pointers/ex_c08_026_8_20_1.c) |
| EX-C08-027 | 教材例程 8.20.2 | 第 8 章 / 8.20.2 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_027_8_20_2.c`](chapters/08-pointers/ex_c08_027_8_20_2.c) |
| EX-C08-028 | 教材例程 8.20.3 | 第 8 章 / 8.20.3 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_028_8_20_3.c`](chapters/08-pointers/ex_c08_028_8_20_3.c) |
| EX-C08-029 | 教材例程 8.21 | 第 8 章 / 8.21 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_029_8_21.c`](chapters/08-pointers/ex_c08_029_8_21.c) |
| EX-C08-030 | 教材例程 custom-03_pointeroutput | 第 8 章 / custom-03_pointeroutput | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_030_03_pointeroutput.c`](chapters/08-pointers/ex_c08_030_03_pointeroutput.c) |
| EX-C08-031 | 教材例程 custom-07_arrayoutput | 第 8 章 / custom-07_arrayoutput | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_031_07_arrayoutput.c`](chapters/08-pointers/ex_c08_031_07_arrayoutput.c) |
| EX-C08-032 | 教材例程 custom-in_class | 第 8 章 / custom-in_class | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_032_in_class.c`](chapters/08-pointers/ex_c08_032_in_class.c) |
| EX-C08-033 | 二维数组指针 | 第 8 章 / custom-pointer | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_033_pointer.c`](chapters/08-pointers/ex_c08_033_pointer.c) |
| EX-C08-034 | 实验演示 lab1-01_pointer | 第 8 章 / lab1-01_pointer | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_034_01_pointer.c`](chapters/08-pointers/ex_c08_034_01_pointer.c) |
| EX-C08-035 | 实验演示 lab1-02_malloc | 第 8 章 / lab1-02_malloc | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_035_02_malloc.c`](chapters/08-pointers/ex_c08_035_02_malloc.c) |
| EX-C08-036 | 实验演示 lab1-04_pointeranalysis | 第 8 章 / lab1-04_pointeranalysis | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_036_04_pointeranalysis.c`](chapters/08-pointers/ex_c08_036_04_pointeranalysis.c) |
| EX-C08-037 | 实验演示 lab5.1 | 第 8 章 / lab5.1 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_037_01.c`](chapters/08-pointers/ex_c08_037_01.c) |
| EX-C08-038 | 实验演示 lab5.2 | 第 8 章 / lab5.2 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_038_02.c`](chapters/08-pointers/ex_c08_038_02.c) |
| EX-C08-039 | 实验演示 lab5.3 | 第 8 章 / lab5.3 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_039_03.c`](chapters/08-pointers/ex_c08_039_03.c) |
| EX-C08-040 | 实验演示 lab5.8 | 第 8 章 / lab5.8 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_040_08.c`](chapters/08-pointers/ex_c08_040_08.c) |
| EX-C08-041 | 实验演示 lab5.9 | 第 8 章 / lab5.9 | 指针、数组与指针、字符串指针、动态内存 | c11-strict | 无 | [`ex_c08_041_09.c`](chapters/08-pointers/ex_c08_041_09.c) |

## 第 9 章 用户自己建立数据类型

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C09-001 | 教材例程 9.1 | 第 9 章 / 9.1 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_001_9_1.c`](chapters/09-user-defined-types/ex_c09_001_9_1.c) |
| EX-C09-002 | 教材例程 9.2 | 第 9 章 / 9.2 | 结构体、枚举、链表、自定义数据类型 | gnu99-textbook | 无 | [`ex_c09_002_9_2.c`](chapters/09-user-defined-types/ex_c09_002_9_2.c) |
| EX-C09-003 | 教材例程 9.3 | 第 9 章 / 9.3 | 结构体、枚举、链表、自定义数据类型 | gnu99-textbook | 无 | [`ex_c09_003_9_3.c`](chapters/09-user-defined-types/ex_c09_003_9_3.c) |
| EX-C09-004 | 教材例程 9.4 | 第 9 章 / 9.4 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_004_9_4.c`](chapters/09-user-defined-types/ex_c09_004_9_4.c) |
| EX-C09-005 | 教材例程 9.5 | 第 9 章 / 9.5 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_005_9_5.c`](chapters/09-user-defined-types/ex_c09_005_9_5.c) |
| EX-C09-006 | 教材例程 9.6 | 第 9 章 / 9.6 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_006_9_6.c`](chapters/09-user-defined-types/ex_c09_006_9_6.c) |
| EX-C09-007 | 教材例程 9.7 | 第 9 章 / 9.7 | 结构体、枚举、链表、自定义数据类型 | gnu99-textbook | 无 | [`ex_c09_007_9_7.c`](chapters/09-user-defined-types/ex_c09_007_9_7.c) |
| EX-C09-008 | 教材例程 9.8 | 第 9 章 / 9.8 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_008_08_ex9_08.c`](chapters/09-user-defined-types/ex_c09_008_08_ex9_08.c) |
| EX-C09-009 | 教材例程 9.9 | 第 9 章 / 9.9 | 结构体、枚举、链表、自定义数据类型 | gnu99-textbook | msvc-crt-compat | [`ex_c09_009_09_ex9_09.c`](chapters/09-user-defined-types/ex_c09_009_09_ex9_09.c) |
| EX-C09-010 | 教材例程 9.10 | 第 9 章 / 9.10 | 结构体、枚举、链表、自定义数据类型 | gnu99-textbook | msvc-crt-compat、malloc-h | [`ex_c09_010_10_ex9_10.c`](chapters/09-user-defined-types/ex_c09_010_10_ex9_10.c) |
| EX-C09-011 | 教材例程 9.11 | 第 9 章 / 9.11 | 结构体、枚举、链表、自定义数据类型 | gnu99-textbook | msvc-crt-compat | [`ex_c09_011_11_ex9_11.c`](chapters/09-user-defined-types/ex_c09_011_11_ex9_11.c) |
| EX-C09-012 | 教材例程 9.12 | 第 9 章 / 9.12 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_012_9_12.c`](chapters/09-user-defined-types/ex_c09_012_9_12.c) |
| EX-C09-013 | 实验演示 lab1-03_structure | 第 9 章 / lab1-03_structure | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_013_03_structure.c`](chapters/09-user-defined-types/ex_c09_013_03_structure.c) |
| EX-C09-014 | 实验演示 lab5.5 | 第 9 章 / lab5.5 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_014_05.c`](chapters/09-user-defined-types/ex_c09_014_05.c) |
| EX-C09-015 | 实验演示 lab5.6 | 第 9 章 / lab5.6 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_015_06.c`](chapters/09-user-defined-types/ex_c09_015_06.c) |
| EX-C09-016 | 实验演示 lab5.7 | 第 9 章 / lab5.7 | 结构体、枚举、链表、自定义数据类型 | c11-strict | 无 | [`ex_c09_016_07.c`](chapters/09-user-defined-types/ex_c09_016_07.c) |

## 第 10 章 对文件的输入输出

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| EX-C10-001 | 教材例程 10.1 | 第 10 章 / 10.1 | 文件、顺序读写、随机读写、错误检测 | gnu99-textbook | 无 | [`ex_c10_001_10_1.c`](chapters/10-files/ex_c10_001_10_1.c) |
| EX-C10-002 | 教材例程 10.2 | 第 10 章 / 10.2 | 文件、顺序读写、随机读写、错误检测 | gnu99-textbook | 无 | [`ex_c10_002_10_2.c`](chapters/10-files/ex_c10_002_10_2.c) |
| EX-C10-003 | 教材例程 10.3.1 | 第 10 章 / 10.3.1 | 文件、顺序读写、随机读写、错误检测 | gnu99-textbook | gets | [`ex_c10_003_10_3_1.c`](chapters/10-files/ex_c10_003_10_3_1.c) |
| EX-C10-004 | 教材例程 10.3.2 | 第 10 章 / 10.3.2 | 文件、顺序读写、随机读写、错误检测 | c11-strict | 无 | [`ex_c10_004_10_3_2.c`](chapters/10-files/ex_c10_004_10_3_2.c) |
| EX-C10-005 | 教材例程 10.4.1 | 第 10 章 / 10.4.1 | 文件、顺序读写、随机读写、错误检测 | gnu99-textbook | 无 | [`ex_c10_005_10_4_1.c`](chapters/10-files/ex_c10_005_10_4_1.c) |
| EX-C10-006 | 教材例程 10.4.2 | 第 10 章 / 10.4.2 | 文件、顺序读写、随机读写、错误检测 | c11-strict | 无 | [`ex_c10_006_10_4_2.c`](chapters/10-files/ex_c10_006_10_4_2.c) |
| EX-C10-007 | 教材例程 10.4.3 | 第 10 章 / 10.4.3 | 文件、顺序读写、随机读写、错误检测 | c11-strict | 无 | [`ex_c10_007_10_4_3.c`](chapters/10-files/ex_c10_007_10_4_3.c) |
| EX-C10-008 | 教材例程 10.5 | 第 10 章 / 10.5 | 文件、顺序读写、随机读写、错误检测 | c11-strict | 无 | [`ex_c10_008_10_5.c`](chapters/10-files/ex_c10_008_10_5.c) |
| EX-C10-009 | 教材例程 10.6 | 第 10 章 / 10.6 | 文件、顺序读写、随机读写、错误检测 | c11-strict | 无 | [`ex_c10_009_10_6.c`](chapters/10-files/ex_c10_009_10_6.c) |
| EX-C10-010 | 教材例程 custom-01_openclose | 第 10 章 / custom-01_openclose | 文件、顺序读写、随机读写、错误检测 | gnu99-textbook | msvc-crt-compat | [`ex_c10_010_01_openclose.c`](chapters/10-files/ex_c10_010_01_openclose.c) |

## 渐进项目

### 计算器

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| PJ-CALC-01 | 计算器渐进项目：步骤 1 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-warning-pragma、msvc-crt-compat | [`step_01.c`](projects/calculator/step_01.c) |
| PJ-CALC-02 | 计算器渐进项目：步骤 2 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-warning-pragma、msvc-crt-compat | [`step_02.c`](projects/calculator/step_02.c) |
| PJ-CALC-03 | 计算器渐进项目：步骤 3 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-warning-pragma、msvc-crt-compat | [`step_03.c`](projects/calculator/step_03.c) |
| PJ-CALC-04 | 计算器渐进项目：步骤 4 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-warning-pragma、msvc-crt-compat | [`step_04.c`](projects/calculator/step_04.c) |
| PJ-CALC-05 | 计算器渐进项目：步骤 5 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-warning-pragma、msvc-crt-compat | [`step_05.c`](projects/calculator/step_05.c) |

### 数据管理

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| PJ-DATA-01 | 数据管理案例：步骤 1 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-crt-compat | [`step_01.c`](projects/data-management/step_01.c) |
| PJ-DATA-02 | 数据管理案例：步骤 2 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-crt-compat | [`step_02.c`](projects/data-management/step_02.c) |
| PJ-DATA-03 | 数据管理案例：步骤 3 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-crt-compat | [`step_03.c`](projects/data-management/step_03.c) |
| PJ-DATA-04 | 数据管理案例：步骤 4 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | msvc-crt-compat | [`step_04.c`](projects/data-management/step_04.c) |

### 贪吃蛇

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| PJ-SNAKE-01 | 贪吃蛇渐进项目：步骤 1 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_01.c`](projects/snake/step_01.c) |
| PJ-SNAKE-02 | 贪吃蛇渐进项目：步骤 2 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_02.c`](projects/snake/step_02.c) |
| PJ-SNAKE-03 | 贪吃蛇渐进项目：步骤 3 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | conio、getch | [`step_03.c`](projects/snake/step_03.c) |
| PJ-SNAKE-04 | 贪吃蛇渐进项目：步骤 4 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | conio、getch | [`step_04.c`](projects/snake/step_04.c) |

### 2048

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| PJ-2048-01 | 2048 渐进项目：步骤 1 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_01.c`](projects/game-2048/step_01.c) |
| PJ-2048-02 | 2048 渐进项目：步骤 2 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_02.c`](projects/game-2048/step_02.c) |
| PJ-2048-03 | 2048 渐进项目：步骤 3 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_03.c`](projects/game-2048/step_03.c) |
| PJ-2048-04 | 2048 渐进项目：步骤 4 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_04.c`](projects/game-2048/step_04.c) |
| PJ-2048-05 | 2048 渐进项目：步骤 5 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_05.c`](projects/game-2048/step_05.c) |
| PJ-2048-06 | 2048 渐进项目：步骤 6 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_06.c`](projects/game-2048/step_06.c) |

### 迷宫

| ID | 标题 | 教材位置 | 知识点 | 编译模式 | 旧语法 | 源码 |
|---|---|---|---|---|---|---|
| PJ-MAZE-01 | 迷宫渐进项目：步骤 1 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_01.c`](projects/maze/step_01.c) |
| PJ-MAZE-02 | 迷宫渐进项目：步骤 2 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | 无 | [`step_02.c`](projects/maze/step_02.c) |
| PJ-MAZE-03 | 迷宫渐进项目：步骤 3 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | conio、getch | [`step_03.c`](projects/maze/step_03.c) |
| PJ-MAZE-04 | 迷宫渐进项目：步骤 4 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | conio、getch | [`step_04.c`](projects/maze/step_04.c) |
| PJ-MAZE-05 | 迷宫渐进项目：步骤 5 | 综合案例 | 综合应用、渐进式开发 | gnu99-textbook | conio、getch | [`step_05.c`](projects/maze/step_05.c) |

## 维护约定

- 不手工维护机器可读目录；索引由源码文件头生成。
- 单个例程的所有源码必须使用同一个例程 ID，且只能有一个 `main()`。
- 编译和运行产物只进入仓库根的隔离临时目录，命令结束时必须删除。
- 本页由 `tools/generate_routine_index.py` 生成。
