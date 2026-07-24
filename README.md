# C 语言程序设计教学仓库

本仓库当前将教学内容划分为“例程、题库、课件”三个板块。本阶段完成的是“例程”板块：以谭浩强《C程序设计（第五版）》第 1–10 章组织195个可追溯例程，并统一使用 MinGW-w64 GCC 验证。

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

## 当前规模

- 例程 ID：195个。
- 严格 C11 例程：104个。
- GNU99 教材兼容例程：91个，其中5个使用 Windows/MinGW 专属接口。
- 内置确定性行为场景：9组。
- 原始源码迁移覆盖：334/334。
- 迁移处置：175项 `canonical_example`、24项 `canonical_project_step`、95项 `merged_duplicate`、39项 `question_bank_pending`、1项 `discarded_after_review`。

## 迁移期边界

- `2023-2024-1/` 与 `2024-2025-1/` 暂时作为只读来源保留。
- `migration/examples-migration.json`、迁移生成器和源码修复规则保留到题库接收39项待迁内容为止。
- 题库确认接收后，先验证334项可追溯，再删除两个旧学年目录；随后将迁移摘要固化到本页，并删除迁移清单与一次性迁移工具。
- 两份教材 PDF 仅作本地参考，已按精确根目录文件名忽略，不得进入 Git。

## 环境约定

- 正式最低基线：MinGW-w64 GCC 8.1。
- CI：Windows 上较新 MinGW-w64 GCC 的向前兼容复验。
- Python：`conda run -n base`，依赖声明见根目录 `requirements.txt`。