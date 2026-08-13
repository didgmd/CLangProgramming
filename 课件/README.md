# C语言程序设计课件

本目录依据《C语言程序设计A》教学大纲组织，共48学时：16次讲授课、8次上机课，每次2课时、每课时45分钟。

当前已完成课次结构、制作约束、CW-L01课程引入PPTX以及CW-L01至CW-L16全部学生端HTML。讲授课采用16:9离线交互式HTML，上机课使用VS Code和GNU GCC完成指定考试型编程题；完整仓库校验仍以Windows MinGW-w64为正式基线。

## 使用入口

- [24课次课程安排](课程安排.md)
- [后续课件制作规范](制作规范.md)
- [往届试卷考点覆盖](往届试卷考点覆盖.md)
- [往届试卷逐题映射](往届试卷题目映射.json)
- [16次讲授课](讲授/README.md)
- [8次上机课](上机/README.md)
- [Windows、macOS和Linux GNU GCC环境配置](../环境配置/README.md)
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
- 上机课中学生独立完成C程序的编写、运行和调试，并将过程与结果填写到教师发放的实验报告模板，最终以PDF格式提交至超星学习通。
- 教材配套PPT继续作为课前预习和课后系统复习材料，课堂HTML不重复覆盖整章教材。
- 往届考点按最相关课次嵌入知识页；学生页面不显示审计过程，且单份HTML不超过36页。

## 当前状态

| 板块 | 数量 | 学时 | 状态 |
|---|---:|---:|---|
| 讲授 | 16次 | 32 | 课次结构完成；CW-L01至CW-L16共16项正式HTML已通过验证 |
| 上机 | 8次 | 16 | CW-LAB01至CW-LAB08正式学生任务单均已通过验证 |
| 合计 | 24次 | 48 | 课程引入PPTX 1项、讲授HTML 16项、上机任务单8项均已完成 |

正式上机任务单属于学生端覆盖证据；学生提交物仅为PDF实验报告。任务单中的参考程序与题库共享题目ID和行为契约，由`tools/validate_labs.py`独立编译、运行并检查结果。

8份历史试卷的242道逻辑题已完成稳定题库映射和学生端证据复核，原件已退役。日常维护通过版本化逐题映射校验来源覆盖，不再依赖原卷文件。

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
