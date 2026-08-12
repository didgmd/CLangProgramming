# C语言程序设计课件

本目录依据《C语言程序设计A》教学大纲组织，共48学时：16次讲授课、8次上机课，每次2课时、每课时45分钟。

当前已完成课次结构、制作约束、CW-L01课程引入PPTX以及CW-L01至CW-L16全部学生端HTML。讲授课采用16:9离线交互式HTML，上机课使用VS Code和MinGW GCC完成指定考试型编程题。

## 使用入口

- [24课次课程安排](课程安排.md)
- [后续课件制作规范](制作规范.md)
- [往届试卷考点覆盖](往届试卷考点覆盖.md)
- [16次讲授课](讲授/README.md)
- [8次上机课](上机/README.md)
- [CW-L01课程引入讨论稿](讲授/01-course-introduction-and-hello-world/课程引入讨论.md)
- [CW-L01课程引入PPTX](讲授/01-course-introduction-and-hello-world/course-introduction.pptx)
- [CW-L01 Hello World HTML](讲授/01-course-introduction-and-hello-world/index.html)
- [CW-L02 基础程序材料 HTML](讲授/02-algorithms-and-program-logic/index.html)
- [CW-L03 顺序程序设计 HTML](讲授/03-sequential-programming/index.html)
- [CW-L04 if条件分支 HTML](讲授/04-selection-if/index.html)
- [CW-L05 嵌套条件与 switch HTML](讲授/05-selection-nesting-and-switch/index.html)
- [CW-L06 循环与状态 HTML](讲授/06-loops-and-state/index.html)
- [CW-L07 嵌套循环 HTML](讲授/07-nested-loops-and-primes/index.html)
- [CW-L08 一维数组 HTML](讲授/08-one-dimensional-arrays/index.html)
- [CW-L09 二维数组与字符串 HTML](讲授/09-matrices-and-strings/index.html)
- [CW-L10 函数、实与形参 HTML](讲授/10-functions-and-parameters/index.html)
- [CW-L11 递归 HTML](讲授/11-recursion/index.html)
- [CW-L12 指针与数组 HTML](讲授/12-pointer-model-and-arrays/index.html)
- [CW-L13 指针参数与字符串复制 HTML](讲授/13-pointer-parameters-and-strings/index.html)
- [CW-L14 结构体 HTML](讲授/14-structures/index.html)
- [CW-L15 结构体数组与指针 HTML](讲授/15-structure-arrays-and-pointers/index.html)
- [CW-L16 文件输入输出 HTML](讲授/16-file-input-and-output/index.html)
- [例程索引](../例程/README.md)
- [题库索引](../题库/README.md)

## 教学原则

- 以学生掌握解题方法、减少失分并通过正考为首要目标。
- 每次讲授只深讲1–2个程序及其知识点和考试题型。
- HTML同时服务课堂投影和课后复习，核心解释不能依赖未写入课件的口头补充。
- 上机课不提供源码骨架，学生根据任务单独立建立、编译、运行和调试C程序。
- 教材配套PPT继续作为课前预习和课后系统复习材料，课堂HTML不重复覆盖整章教材。
- 往届考点按最相关课次嵌入知识页；学生页面不显示审计过程，且单份HTML不超过36页。

## 当前状态

| 板块 | 数量 | 学时 | 状态 |
|---|---:|---:|---|
| 讲授 | 16次 | 32 | 课次结构完成；CW-L01至CW-L16共16项正式HTML已通过验证 |
| 上机 | 8次 | 16 | 目录与设计契约完成，正式任务单为0 |
| 合计 | 24次 | 48 | 结构规划完成，正式PPTX已完成1项、讲授HTML已完成16项 |

`QB-PG-041`和`QB-PG-042`是上机1、上机8的题库前置任务，目前只保留编号与任务定义，不创建失效链接。正式制作对应上机任务单前，必须先将两题补入题库并通过题库校验。

CW-L01 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L01
```

CW-L02 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L02
```

CW-L03 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L03
```

CW-L04 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L04
```

CW-L05 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L05
```

CW-L06 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L06
```

CW-L07 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L07
```

CW-L08 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L08
```

CW-L09 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L09
```

CW-L10 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L10
```

CW-L12 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L12
```

CW-L13 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L13
```

CW-L14 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L14
```

CW-L15 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L15
```

CW-L16 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L16
```
