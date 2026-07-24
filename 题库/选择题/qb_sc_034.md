<!-- question-meta
id: QB-SC-034
category: 选择题
chapters: 5
concepts: continue、循环控制
difficulty: 基础
minutes: 2
related_routines: 无
compile_mode: none
legacy_features: 无
-->
# continue死循环

## 题目

循环中当 `i==3` 时立即执行 `continue`，但 `i` 的自增写在其后，可能导致（ ）。

A. 正常结束

B. 只少加一次

C. 死循环

D. 编译错误

## 常见失分点



本题考查“continue死循环”（continue、循环控制）。逐项代入C语言规则核对，尤其不要把看起来熟悉的写法直接当作合法答案。

<details>
<summary>参考答案与解析</summary>

**答案：C。**

命中 `continue` 后自增被跳过，`i` 永远停在 3。

</details>
