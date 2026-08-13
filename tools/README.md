# 仓库维护工具

本页面向仓库维护者，不是学生入门必读材料。本目录保存当前正式维护链路中的10个Python脚本。命令行入口负责校验或生成索引，共享模块由这些入口导入；共享模块没有独立命令入口并不表示其生命周期已经结束。

## 命令行入口

| 脚本 | 职责 | 直接调用 |
|---|---|---|
| `validate_routines.py` | 校验例程元数据、目录、编译、行为、索引、退役根目录制品及历史迁移残留 | `conda run -n base python tools/validate_routines.py` |
| `validate_questions.py` | 校验题库结构、答案、程序、行为、索引和往届试卷映射 | `conda run -n base python tools/validate_questions.py` |
| `validate_courseware.py` | 校验CW-L01至CW-L16的HTML结构、交互、本地链接和课程专属契约 | `conda run -n base python tools/validate_courseware.py --id CW-L01` |
| `validate_labs.py` | 校验8份上机任务单、参考程序和确定性行为结果 | `conda run -n base python tools/validate_labs.py` |
| `generate_routine_index.py` | 生成或检查例程索引 | `conda run -n base python tools/generate_routine_index.py --check` |
| `generate_question_index.py` | 生成或检查题库索引 | `conda run -n base python tools/generate_question_index.py --check` |

生成器去掉`--check`时会更新对应索引；日常验收优先使用只读检查模式。

## 共享内部模块

| 模块 | 使用方 | 职责 |
|---|---|---|
| `routine_common.py` | 例程生成器、例程校验器 | 例程元数据、路径和索引共享逻辑 |
| `question_common.py` | 题库生成器、题库校验器、课件校验器 | 题目解析、稳定ID和题库路径共享逻辑 |
| `question_quality.py` | 题库校验器 | 题干、答案和排版质量规则 |
| `question_program_quality.py` | 题库校验器 | C代码块、参考程序和行为契约质量规则 |

## 生命周期规则

- 上述10个脚本均为`active`，本轮没有可删除的现存脚本。
- `migrate_examples.py`、`source_fixes.py`等一次性迁移脚本已经退役，校验器会阻止旧迁移脚本、目录和构建残留重新进入仓库。
- 删除或合并工具前，应先检查其他工具的导入关系、GitHub Actions和文档入口，再运行受影响的全部校验器。
- 共享模块属于内部接口；不得仅因它们不能直接执行而判定为冗余。
- Python工具只使用标准库；课程C程序的临时源码和运行产物由校验器在隔离临时目录中创建并清理。

## 内容与历史契约

- 例程库固定为195个稳定ID，题库固定为173道题，上机任务单固定为8份；数量变化必须同时修改内容契约和相应校验器。
- 8份历史试卷已经由242条逐题映射和学生端证据吸收，日常题库校验读取版本化映射，不依赖原卷。
- 两份教材PDF、教学大纲DOC和MinGW压缩包已经退役；`validate_routines.py`检查这些制品没有重新出现在根目录、Git跟踪或`.gitignore`中。
- 源码头保留教材位置和历史来源字符串。来源证据不表示第三方内容自动适用仓库MIT许可证，授权边界见[第三方内容与来源说明](../THIRD_PARTY_NOTICES.md)。

## CI与诊断

- [GitHub Actions](../.github/workflows/routines.yml)在Windows上定位MinGW-w64 GCC，并运行例程、题库和上机任务单校验。
- 正式最低编译基线为MinGW-w64 GCC 8.1；CI使用较新版本进行向前兼容复验。
- `EX-C06-012`保留无`\0`字符数组与`%s`的教学诊断，并使用例程级允许规则；其他新告警仍会导致失败。
- MSVC兼容pragma仅在源码声明相应旧语法且诊断精确匹配时允许，不通过全局关闭警告放宽校验。

## 发布前检查

```powershell
conda run -n base python tools/generate_routine_index.py
conda run -n base python tools/generate_question_index.py
conda run -n base python tools/validate_routines.py
conda run -n base python tools/validate_questions.py
conda run -n base python tools/validate_labs.py

$ids = 1..16 | ForEach-Object { "CW-L{0:D2}" -f $_ }
foreach ($id in $ids)
{
    conda run -n base python tools/validate_courseware.py --id $id
}

conda run -n base python tools/generate_routine_index.py --check
conda run -n base python tools/generate_question_index.py --check
git diff --check
```

校验过程必须保持仓库中无`.exe`、`.o`、`.obj`、缓存、截图或临时服务器残留。所有新增或修改文本使用UTF-8无BOM和LF。
