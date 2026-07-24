# CW-L01 课程引入PPT：gpt-image-2提示词清单

- 课次：`CW-L01`
- 用途：`course-introduction.pptx`的8页视觉素材记录
- 生成方式：内置 `image_gen`，每页单独生成
- 视觉类型：`scientific-educational`
- 输出构图：16:9课堂投影视觉；中文标题、论点、箭头和流程由PPTX文本层添加
- 生成状态：8页素材均已选定并嵌入PPTX
- 署名：`Kevin@SUT`

## 统一视觉前缀

```text
Use case: scientific-educational
Asset type: 16:9 classroom presentation visual
Style/medium: polished editorial illustration, semi-flat painterly forms, restrained cinematic depth, coherent educational metaphor
Color palette: deep graphite, cool cyan, muted slate, warm amber accents, occasional off-white highlights
Lighting/mood: cool cyan system light balanced by warm amber human agency; curious, serious, hopeful, never dystopian
Composition: wide 16:9, preserve a clean text-safe area for the PPTX text layer, keep the visual subject away from the primary Chinese title area
Text: none
Constraints: no text, no letters, no numbers, no readable code, no logos, no watermark, no formulas, no famous people, no exam papers, no textbook pages, no third-party imagery; Chinese information is added by the PPTX text layer
```

## Slide 01：AI会写代码，我为什么还学C？

- 视觉用途：封面主视觉，提出学生最可能的疑问。
- 主体关系：右侧学生面对抽象AI工作站和代码墙，左侧保持安静留白。
- 构图与裁切：人物、桌面和AI光源位于右侧；左侧至少保留约42%的深色标题安全区；PPTX使用全幅`cover`。
- 色彩与情绪：深石墨、冷青屏幕光、少量暖琥珀轮廓光；好奇、严肃、非末日化。
- 教学隐喻：学生面对一个可以生成候选代码的AI，但仍需要提出问题。
- 负面约束：无文字、无Logo、无水印、无可读代码、无复杂公式、无名人、无教材扫描页、无试卷、无第三方图片。
- 生成提示：`A thoughtful first-year student on the right faces a softly luminous AI workstation and an abstract wall of glowing code-like lines in a dark graphite learning studio; leave the left 42 percent calm and dark for a Chinese title; editorial illustration, cool cyan and warm amber accents; no text, no readable code, no logo, no watermark; Chinese title will be added by the PPTX text layer.`

## Slide 02：代码生成变快了，问题没有消失

- 视觉用途：表现人类提出目标、AI生成多个候选实现。
- 主体关系：左侧人类在空白板前提出目标，右侧三个AI工作站提供不同候选流。
- 构图与裁切：左侧保留标题区；人类位于左中部，候选流横向展开至右侧；不让候选流进入标题安全区。
- 色彩与情绪：人类动作用暖琥珀，候选流用冷青；协作而非替代。
- 教学隐喻：候选方案变多，并不等于“什么才算完成”已经被定义。
- 负面约束：无文字、无Logo、无水印、无可读代码、无复杂公式、无名人、无教材扫描页、无试卷、无第三方图片。
- 生成提示：`A first-year student on the left sketches a goal on a blank board; three luminous abstract AI workstations on the right produce different candidate solution streams; dark graphite studio, editorial illustration, warm human planning light and cool cyan candidate streams; wide 16:9 with clean left text-safe area; no text, no labels, no readable screens, no logos, no watermark.`

## Slide 03：代码生成只是交付链的一环

- 视觉用途：把候选代码与需求、接口、测试、风险、交付责任区分开。
- 主体关系：左侧抽象代码流来自AI，右侧人类在工程工作台上检查流程和边界。
- 构图与裁切：中央和左上留出PPTX标题与对照文字区域；人和验证工作台集中在右侧。
- 色彩与情绪：AI候选流冷青，工程检查点暖琥珀；理性、可审查、有责任感。
- 教学隐喻：生成速度只是链条的一段，工程价值来自可验证的交付。
- 负面约束：无文字、无Logo、无水印、无可读代码、无复杂公式、无名人、无教材扫描页、无试卷、无第三方图片。
- 生成提示：`An abstract cyan stream of candidate code-like fragments enters a grounded engineering workbench on the right; a human reviewer checks requirements, interfaces, tests, risk, and delivery through symbolic instruments and connected boards; dark graphite editorial illustration, warm amber checkpoints, clean text-safe left area, no readable text or code, no logos or watermark.`

## Slide 04：C把程序运行变得可观察

- 视觉用途：将C呈现为观察程序状态和失败边界的透明实验室。
- 主体关系：右侧学生观察透明玻璃程序舱，舱内有抽象状态节点、内存块、输入输出和边界线。
- 构图与裁切：左侧保持深色文字安全区；透明实验室占据右侧；所有符号必须是抽象图形而非可读代码。
- 色彩与情绪：舱内冷青，边界线暖琥珀；精确、可观察、适合零基础学生理解。
- 教学隐喻：程序状态只有被看见，才可能被验证和修正。
- 负面约束：无文字、无Logo、无水印、无可读代码、无复杂公式、无名人、无教材扫描页、无试卷、无第三方图片。
- 生成提示：`A transparent glass-like program laboratory on the right contains abstract glowing nodes, memory blocks, state paths, input and output streams, and warm boundary markers; a student observes from the right; dark graphite educational editorial illustration, cool cyan internal light and warm amber boundary light; preserve the left 38 percent for Chinese text; no readable code, no formulas, no labels, no logo, no watermark.`

## Slide 05：项目里，谁来定义“完成”？

- 视觉用途：表现人在需求、验收、测试、风险和交付节点作决定。
- 主体关系：人类沿着一条暖色决策路径前进，右下AI提供多个冷青候选选项。
- 构图与裁切：左侧保留标题和结论文字；路径从右下延伸至右上终点；底部留出可编辑流程节点带。
- 色彩与情绪：人的决策节点暖琥珀，AI候选冷青；坚定、清晰、可追责。
- 教学隐喻：AI可以提供选项，但“完成”的定义和风险承担属于人。
- 负面约束：无文字、无Logo、无水印、无可读代码、无复杂公式、无名人、无教材扫描页、无试卷、无第三方图片。
- 生成提示：`A human project lead walks along a path of warm amber decision checkpoints toward a completed delivery on the right; cool cyan abstract candidate options arrive from an AI station but do not decide; dark graphite project room, wide 16:9, calm left text-safe area, editorial illustration; no text, no labels, no logos, no watermark.`

## Slide 06：只点“同意”，可能完成任务，却失去思考

- 视觉用途：对比被动点击同意与主动解释、测试、修改。
- 主体关系：左侧低对比度被动学生面对单一确认手势；右侧学生检查候选方案、边界和修改路径。
- 构图与裁切：画面中部保留自然分界；标题与定义放上方；两栏标签由PPTX覆盖在下方。
- 色彩与情绪：左侧灰蓝、右侧冷青与暖琥珀；不羞辱学生，强调可改变的协作习惯。
- 教学隐喻：问题不在使用AI，而在把思考、验证和责任全部外包。
- 负面约束：无文字、无Logo、无水印、无可读代码、无复杂公式、无名人、无教材扫描页、无试卷、无第三方图片。
- 生成提示：`A compassionate split scene: on the left a low-contrast passive student faces a glowing approval gesture; on the right an engaged student reviews a candidate solution, checks a boundary, and edits a plan; dark graphite editorial illustration, cool gray-blue left, cyan and warm amber right, no text, no labels, no logos, no watermark.`

## Slide 07：保留认知主权：先想，再问，再验证

- 视觉用途：表现定义、预测、生成、检查、测试、解释、决策的闭环。
- 主体关系：右侧学生围绕一条冷青与暖琥珀相间的圆形路径前进，七个抽象站点环绕路径。
- 构图与裁切：左侧留出标题和解释文字；环形路径占右侧；节点名称和箭头由PPTX覆盖。
- 色彩与情绪：循环路径冷青，决策站点暖琥珀；稳定、反思、保留人的能动性。
- 教学隐喻：AI可以进入循环，但不能删掉人的定义、验证、解释和决策步骤。
- 负面约束：无文字、无Logo、无水印、无可读代码、无复杂公式、无名人、无教材扫描页、无试卷、无第三方图片。
- 生成提示：`A student carrying a notebook walks around a large luminous circular path with seven abstract learning stations; cyan and warm amber loop, dark graphite learning space, hopeful educational editorial illustration, preserve the left 38 percent for Chinese title and explanation, no labels or arrows in the image, no text, no logo, no watermark.`

## Slide 08：本课程的学习契约

- 视觉用途：把AI协作闭环落到C语言、Hello World、例程、题库和上机。
- 主体关系：学生从暗色AI协作空间走进明亮课堂，右侧出现空白屏幕和第一课入口。
- 构图与裁切：左侧保留学习契约文字；学生和课堂门口位于右侧；画面有明确的温暖终点。
- 色彩与情绪：后方冷青逐渐过渡到前方暖琥珀和柔和日光；欢迎但不幼稚。
- 教学隐喻：课程不是拒绝AI，而是建立能定义、写出、测试、解释和修改程序的能力。
- 负面约束：无文字、无Logo、无水印、无可读代码、无复杂公式、无名人、无教材扫描页、无试卷、无第三方图片。
- 生成提示：`A student steps from a cool cyan AI collaboration space into a warm, clear first programming classroom through a bright gateway on the right; blank screen and board with no writing, subtle path leading to a first lesson; dark graphite to warm classroom transition, wide 16:9, clean left text-safe area, no text, no labels, no logos, no watermark.`

## 嵌入与生命周期

- 8张图只作为PPTX嵌入素材使用。
- 最终不保留PNG/JPG/WebP原图、生成过程文件、渲染图或源脚本。
- PPTX中的中文标题、流程、标签和页脚均为可编辑文本或形状，不依赖图像中的文字。
- 若后续需要替换单页视觉，只重新生成对应页，不改变稳定课次ID和PPTX文本接口。