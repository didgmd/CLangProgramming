# C语言程序设计课件

本目录依据《C语言程序设计A》教学大纲组织，共48学时：16次讲授课、8次上机课，每次2课时、每课时45分钟。

当前已完成课次结构、制作约束、CW-L01课程引入PPTX和Hello World HTML交互课件；CW-L02已完成25页学生端HTML，两个45分钟教学段严格分离，其余课件和上机源码仍未制作。讲授课采用16:9离线交互式HTML，上机课使用VS Code和MinGW GCC完成指定考试型编程题。

## 使用入口

- [24课次课程安排](课程安排.md)
- [后续课件制作规范](制作规范.md)
- [16次讲授课](讲授/README.md)
- [8次上机课](上机/README.md)
- [CW-L01课程引入讨论稿](讲授/01-course-introduction-and-hello-world/课程引入讨论.md)
- [CW-L01课程引入PPTX](讲授/01-course-introduction-and-hello-world/course-introduction.pptx)
- [CW-L01 Hello World HTML](讲授/01-course-introduction-and-hello-world/index.html)
- [CW-L02 基础程序材料 HTML](讲授/02-algorithms-and-program-logic/index.html)
- [例程索引](../例程/README.md)
- [题库索引](../题库/README.md)

## 教学原则

- 以学生掌握解题方法、减少失分并通过正考为首要目标。
- 每次讲授只深讲1–2个程序及其知识点和考试题型。
- HTML同时服务课堂投影和课后复习，核心解释不能依赖未写入课件的口头补充。
- 上机课不提供源码骨架，学生根据任务单独立建立、编译、运行和调试C程序。
- 教材配套PPT继续作为课前预习和课后系统复习材料，课堂HTML不重复覆盖整章教材。

## 当前状态

| 板块 | 数量 | 学时 | 状态 |
|---|---:|---:|---|
| 讲授 | 16次 | 32 | 课次结构完成；CW-L01正式HTML 1项、CW-L02 25页正式HTML 1项已通过验证 |
| 上机 | 8次 | 16 | 目录与设计契约完成，正式任务单为0 |
| 合计 | 24次 | 48 | 结构规划完成，正式PPTX已完成1项、讲授HTML已完成2项，CW-L02严格分段版已交付 |

`QB-PG-041`和`QB-PG-042`是上机1、上机8的题库前置任务，目前只保留编号与任务定义，不创建失效链接。正式制作对应上机任务单前，必须先将两题补入题库并通过题库校验。

CW-L01 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L01
```

CW-L02 HTML的日常校验命令：

```powershell
conda run -n base python tools/validate_courseware.py --id CW-L02
```
