# C 语言程序设计教学仓库

本仓库将教学内容划分为“例程、题库、课件”三个板块。当前已完成例程库与第一版题库，并建立课件板块的24课次结构：例程按谭浩强《C程序设计（第五版）》第 1–10 章组织，题库按常见考试题型组织，统一使用 MinGW-w64 GCC 验证。课件已完成CW-L01课程引入PPTX、提示词和Hello World HTML交互课件，以及严格按两个45分钟教学段组织的CW-L02至CW-L15学生端HTML。

## 四条最短路径

### 1. 按教材章节查找

打开[例程索引](例程/README.md)，可按章节、教材位置、知识点、项目步骤或旧语法查找源码。

### 2. 直接使用 MinGW GCC 编译

单文件严格例程：

```powershell
gcc -std=c11 -Wall -Wextra -Wpedantic -Werror "例程/chapters/01-programming-and-c/ex_c01_001_1_1.c" -o hello.exe
.\hello.exe
Remove-Item -LiteralPath .\hello.exe
```

教材兼容例程使用 `-std=gnu99 -Wall -Wextra`。多文件例程建议通过下方校验器按 ID 整体构建。

### 3. 验证全部或单个例程

```powershell
# 全量结构、编译和行为验证
conda run -n base python tools/validate_routines.py

# 验证单个例程
conda run -n base python tools/validate_routines.py --id EX-C05-010

# 检查例程索引是否最新
conda run -n base python tools/generate_routine_index.py --check
```

Python 工具仅使用标准库，不会自动安装软件包。编译和运行均发生在仓库根的隔离临时目录，命令结束时自动删除，最终必须无过程产物。

### 4. 识别教材旧语法

每个源码文件头都声明：例程 ID、标题、教材位置、知识点、来源、编译模式、旧语法、交互方式和兼容性。

- `c11-strict`：使用 `-std=c11 -Wall -Wextra -Wpedantic -Werror`。
- `gnu99-textbook`：使用 `-std=gnu99 -Wall -Wextra`，用于教材兼容写法和 Windows 接口。
- `gets()` 只在具有教材识别价值的例程中受控保留；必须使用短输入，且不得在生产程序中照搬。
- `conio.h`、`getch()` 等接口仅以 MinGW-w64 GCC 环境为验证边界。

## 学生题库

打开[题库索引](题库/README.md)，可按选择题、判断题、程序填空、读程序写结果和编程题独立练习。每道题的参考答案与解析均保存在同一 Markdown 文件的折叠区域中。

```powershell
# 全量检查题目结构、索引和参考程序
conda run -n base python tools/validate_questions.py

# 检查一道题
conda run -n base python tools/validate_questions.py --id QB-PG-001

# 检查题库索引是否最新
conda run -n base python tools/generate_question_index.py --check
```

## 课件

打开[课件索引](课件/README.md)，可查看16次讲授课、8次上机课的安排及后续制作规范。每次讲授为2课时，围绕1–2个程序展开；每次上机为2课时，使用VS Code和MinGW GCC独立完成1道考试型编程题。

当前课件板块包含课次目录、课程安排、设计契约、CW-L01课程引入PPTX和Hello World HTML，以及已通过回归校验的CW-L02、CW-L03两份25页、CW-L04和CW-L05两份26页、CW-L06一份28页、CW-L07和CW-L08两份30页、CW-L09和CW-L11两份34页、CW-L10一份32页、CW-L12至CW-L14三份36页、CW-L15一份35页学生端HTML；CW-L16 HTML、图片素材和上机源码骨架仍未制作。

## 当前规模

- 例程 ID：195个。
- 严格 C11 例程：104个。
- GNU99 教材兼容例程：91个，其中5个使用 Windows/MinGW 专属接口。
- 内置确定性行为场景：9组。
- 原始源码迁移覆盖：334/334。
- 迁移处置：175项 `canonical_example`、24项 `canonical_project_step`、95项 `merged_duplicate`、39项 `question_bank_received`、1项 `discarded_after_review`。
- 题库：172道，其中选择题65道、判断题14道、程序填空22道、读程序写结果31道、编程题40道。
- 题库内嵌可编译参考程序：62个。
- 8份本地试卷的242个完整题干经复核、规范化和语义去重后形成146道真题型练习；另由39项旧内容构造26道新题。
- 题库内置正常与边界行为场景：76组；40/40道编程题样例和31/31道读程序输出均执行比对。
- 程序审计：93/93道含程序题、115/115个C代码块完成复核；62个完整参考程序全部通过MinGW-w64 GCC 8.1编译。
- 代码排版：多层控制语句同行、控制头与执行语句同行、Tab、非允许超长行、数组下标前空格和同行堆叠普通语句均为0。
- 课件规划：16次讲授课、8次上机课，讲授32学时、上机16学时，共48学时；当前完成度为结构规划24/24、课程引入PPTX 1/16、讲授HTML 15/16，其中CW-L02、CW-L03均为25页，CW-L04、CW-L05均为26页，CW-L06为28页，CW-L07、CW-L08均为30页，CW-L09、CW-L11均为34页，CW-L10为32页，CW-L12至CW-L14均为36页，CW-L15为35页学生端课件。
- 原题证据链：8份本地试卷的242/242个题干完成两轮迁移期核对；修订清单及OCR/页面过程文件在验收后清除。


## 题库修订验收

- 完整题干、选项、程序、输入输出条件与样例已按题型补齐；不再使用统一的泛化失分提醒或测试说明。
- 22道程序填空题均包含编号空位、逐空答案和与题目一致的还原程序；原先错配的参考程序已全部替换。
- 40道编程题均包含输入格式、输出格式、数据范围、样例、评分建议、正常与边界测试和完整参考程序。
- 日常校验器会拒绝单行完整函数、Tab、异常长行、同行堆叠语句、缺失选项或答案、缺失输入输出及样例等退化内容。
- MinGW-w64 GCC验证结果：62个内嵌参考程序、76组确定性行为场景、40道编程题样例和31道读程序输出全部通过。
- 程序填空题会自动比较“逐空答案代回后的程序”与完整参考程序；39项旧内容的交接状态由稳定题目 ID 的 39/39 契约校验，原始语义审计保留在 Git 历史中。

## 历史来源清理状态

- 334/334 个原始源码已完成迁移审计；清理前统计为 175 项 `canonical_example`、24 项 `canonical_project_step`、95 项 `merged_duplicate`、39 项 `question_bank_received` 和 1 项 `discarded_after_review`。
- `2023-2024-1/`、`2024-2025-1/`、`migration/` 及一次性迁移工具已从工作区移除；原始路径、哈希和处置关系可通过 Git 历史追溯。
- 39/39 项旧内容已交接到题库，对应 26 个稳定题目 ID；日常题库校验器只检查稳定 ID，不依赖旧学期目录。
- 例程源码头中的“来源”字段保留历史 provenance 字符串；这些路径不再表示当前工作区中的可访问目录。
- 两份教材 PDF、教学大纲 DOC 和 8 份历史试卷原文件仅作为后续课件制作的本地参考，按精确根目录文件名忽略，未进入 Git，且不移动、不修改。
- 日常仓库只保留例程、题库、课件、索引器和校验器；编译、运行、审计、渲染和转录产物不作为仓库内容保存。
## 环境约定

- 正式最低基线：MinGW-w64 GCC 8.1。
- CI：Windows 上较新 MinGW-w64 GCC 的向前兼容复验。
- Python：`conda run -n base`，依赖声明见根目录 `requirements.txt`。

## GitHub Actions CI

[GitHub Actions 工作流](.github/workflows/routines.yml) 在 Windows `windows-latest` 上使用 `msys2/setup-msys2` 的动态安装路径定位 MinGW GCC，再分别运行例程和题库校验器。CI 不依赖本地教材、试卷或其他被忽略参考资料；失败时仅将验证日志作为 7 天的 Actions 诊断产物保存，不写入仓库。CI 使用较新 MinGW-w64 GCC 做向前兼容复验，本地最低基线仍为 GCC 8.1。

## 教学诊断与告警策略

- `EX-C06-012` 明确保留无 `\0` 字符数组与 `%s` 的风险演示；其已确认的 GCC 教学诊断只按例程 ID 精确允许，其他新告警仍会导致校验失败。
- MSVC 兼容 pragma 的 GCC 忽略提示仅在源码声明 `msvc-warning-pragma` 且诊断文本精确匹配时允许，不通过全局 `-w` 或删除 `-Werror` 放宽质量门槛。
- GitHub Actions 保持启用；遇到新的编译器诊断时优先修复源码或补充有证据的例程级规则。
