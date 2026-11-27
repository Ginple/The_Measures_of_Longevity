# 市场与读者定位（第一轮）｜Market & Reader Positioning, Round 1

- **日期**：2026-11-27（UTC）
- **状态**：**研究启动稿，不是出版决策**。
  - 结论来自公开网页的一轮检索：行业统计、书店榜单、书评与媒体报道。
  - **没有** Circana BookScan、Nielsen BookData 或出版社的销量数据。
  - 第三方网页上的销量和排名估计只能当作方向信号。
- **市场优先级**（作者指定）：
  1. 美国、加拿大；
  2. 其他英语国家（英国、澳大利亚、新西兰、印度等）；
  3. 简体中文、繁体中文、日本。
- **书名**：作者已锁定《长寿的尺度》/ *The Measures of Longevity*（见 [BOOK_PROPOSAL](../BOOK_PROPOSAL.md)）。本文不提出改名。
- **关联**：
  - [DEC-011 章节地图](../manuscript/OUTLINE_v1.md)；
  - [架构决定](../ARCHITECTURE_DECISION_2026-11-27.md)；
  - [台账 X147](../../knowledge_base/CLAIM_LEDGER.md)（英文版篇幅与 33 章结构的冲突）。

来源证据等级：
- **A**：行业机构或官方统计（AAP、BookNet Canada、出版科学研究所、APA）；
- **B**：零售商页面、出版社页面或主流媒体；
- **C**：博客、营销网站、第三方估算。只作线索，不引用具体数字。

---

## 0. 一句话定位（工作版）

> **For readers who already track their health — or are being sold tests that claim to — *The Measures of Longevity* is the book that explains what longevity numbers can and cannot tell you, how to judge claims that someone has "become younger," and why a longer life only matters if it remains a life worth living.**
>
> 中文工作版：写给已经在测量自己、或正被推销各种"生物年龄"检测的读者。它解释长寿数字能说明什么、不能说明什么，怎样判断"变年轻"的说法，以及为什么更长的生命只有在仍值得过时才有意义。

**与竞品的区别**（只描述定位，不评价质量）：

| 竞品 | 它们给读者的东西 | 本书给读者的东西 |
|---|---|---|
| Attia《Outlive》 | 个人行动方案 | 读懂和判断方案背后测量的方法 |
| Sinclair《Lifespan》 | 机制乐观叙事 | 机制主张的可识别性边界 |
| Ramakrishnan《Why We Die》 | 衰老生物学的冷静叙述 | 把这种冷静落到具体测量（水平、速率、恢复、余量），并延伸到生活条件（卷Ⅲ） |
| Buettner《Blue Zones》 | 生活方式与社区 | 吸收"生活条件"维度，但不讲长寿地带神话 |

---

## 1. 市场事实（按优先级）

### 1.1 美国（优先级 1）

| 事实 | 数字 | 来源 | 等级 |
|---|---|---|---|
| 美国出版总收入，2025 | 334 亿美元（+2.5%）；大众（trade）217 亿美元（+2.7%） | [AAP StatShot Annual 2025，经 infoDOCKET 转载](https://www.infodocket.com/2026/08/10/new-data-from-the-association-of-american-publishers-aap-publishing-revenues-totaled-33-4-billion-for-calendar-year-2025/) | A |
| 成人非虚构，2025 | 60 亿美元（+1.3%）；册数 −0.3%，增长全部来自价格 | 同上；[册数解读](https://all-about-digital-publishing.com/en/2026/aap-2025) | A / C |
| 数字格式，2025 | 有声书 25 亿美元（+5.3%）> 电子书 22 亿美元（+3.2%）；数字合计占 14.2% | AAP（同上） | A |
| 有声书出版商口径，2025 | 24.3 亿美元（+9%）；AI 朗读仅占收入 0.03%，愿意尝试 AI 朗读的比例从 70% 降到 61% | APA 2026 调查，经[解读文章](https://all-about-digital-publishing.com/en/2026/aap-2025)转述 | A（二手转述） |
| 阅读格式，2025 年 10 月 | 过去一年 64% 美国成人读过纸书、31% 读过电子书、26% 听过有声书 | Pew Research Center，经[统计汇编](https://extypis.app/en/writing-publishing-statistics)转述 | A（二手转述） |
| 亚马逊"Aging"榜头部（检索时） | Means《Good Energy》、Attia《Outlive》、《Ikigai》、Buettner《Blue Zones Kitchen》、Wright《Unbreakable》、Topol《Super Agers》、Gupta《Keep Sharp》、Longo《The Longevity Diet》等 | [Amazon Best Sellers: Aging（节点 282840）](https://www.amazon.com/gp/bestsellers/books/282840) | B（快照，随时变化） |
| 以时钟为中心的大众书表现有限 | Morgan Levine《True Age》在 Goodreads 约 128 个评分；Steele《Ageless》约 1,500；Brendborg《Jellyfish Age Backwards》约 6,000 | [Goodreads 长寿书架](https://www.goodreads.com/shelf/show/life-extension) | B（评分数只是读者规模的弱代理） |
| 消费级"生物年龄"检测市场 | Function Health 称会员超过 50 万（年费 365 美元）；TruDiagnostic 称已检测超过 12 万例；"没有一种被证明能让人更健康" | [NewMarketPitch 2026-11](https://newmarketpitch.com/blogs/news/longevity-who-is-ahead-biological-age-tests)、[2026-10](https://newmarketpitch.com/blogs/news/longevity-business-model) | C（公司自报，经第三方汇总） |
| 对《Outlive》的主要批评 | 依赖观察性研究推断因果（VO2max）；检测偏多、可能过度诊断；生物标志物与结局关系不清；纳入研究以男性为主 | [LessWrong 评论](https://www.lesswrong.com/posts/QqTiCz2Xz96MuEFsF/outlive-a-critical-review)、[Keep Health](https://keep.health/outlive-book-review-the-science-and-art-of-longevity/)、[TopDoctor 2026](https://topdoctormagazine.com/biohacking/outlive-science-art-longevity-paperback-review/) | C |

**解读**：
1. **需求在，但册数不增长。** 成人非虚构靠涨价增长，读者数量没有扩大。新书要从现有长寿读者那里分走注意力，而不是等市场自己变大。
2. **"测完之后怎么读数"是空位。**
   - 头部书主要卖两类东西：行动方案（Outlive、Good Energy、Longevity Diet）和生活方式（Blue Zones、Ikigai）。
   - 与此同时，消费级检测的买家已达数十万人，而第三方汇总也承认这些检测"没有被证明能改善健康"。
   - 《True Age》说明，**只讲时钟本身**的书没有打开市场。本书不能定位为"时钟书"，而要定位为**"测量素养 + 生活判断"**：时钟只是第 5 章的一个案例。
3. **对头部书的批评正好是本书的方法核心**：因果与观察的区别、检测带来的过度诊断、标志物与结局分离（第 4、5、18、29 章）。这些可以作为卖点，但**不得以攻击具体作者的方式营销**。
4. **有声书优先级高于电子书**，且应由真人朗读。本书表格多，有声版需要配套 PDF。

### 1.2 加拿大（优先级 1）

| 事实 | 数字 | 来源 | 等级 |
|---|---|---|---|
| 纸书零售，2025 | 11.46 亿加元，约 4,793 万册（+4.1%）；非虚构占 30% | [BookNet Canada 2026-03-31](https://www.booknetcanada.ca/blog/2026/3/31/the-canadian-book-market-2025)；[PW](https://www.publishersweekly.com/pw/by-topic/international/international-book-news/article/100051-canadian-print-book-sales-rose-4-1-in-2025.html) | A |
| 加拿大作者份额 | 14%（2024 年为 12%），被解读为"买加拿大货"情绪 | 同上 | A |
| 非虚构头部 | Robbins《The Let Them Theory》；Podleski《Every Salad Ever》（自出版） | 同上 | A |
| 分销商口径的健康类增长 | Health & Fitness +70%，Medical +196% | [PublishDrive](https://publishdrive.com/canada-book-market-2025-how-canadian-ebooks-print-books-and-audiobooks-performed.html) | C（单一分销商，不代表全市场） |

**解读**：
- 美加共用同一个英文版。加拿大需要做的本地化：
  - 公制单位优先，美制并列；
  - 用加拿大的数据与制度举例。例如加拿大纵向老龄研究（CLSA）；公共医保下，直接面向消费者的检测在各省的可及性与监管不同。
- 卷Ⅲ（住房、照护、不平等）在加拿大语境下要避免只写美国的医疗体系。
- 在加拿大，自出版书可以做到非虚构第二，说明独立渠道可行，但这本身不构成选择渠道的理由。

### 1.3 其他英语国家（优先级 2）

- **英国**：非虚构 2025 年下降 3%，至约 10 亿英镑；小说和童书增长（[解读文章](https://all-about-digital-publishing.com/en/2026/aap-2025)，C 级转述）。英国读者熟悉 UK Biobank，本书大量证据来自 UK Biobank，这是天然的连接点。版权通常由英国出版社单独购买；拼写与单位要另出一版。
- **澳大利亚、新西兰**：通常随英国版或美国版发行。本轮**没有**检索到本地数据，待补。
- **印度**：价格敏感，通常出本地平装版。本轮**没有**检索到本地数据，待补。

### 1.4 简体中文、繁体中文、日本（优先级 3）

| 市场 | 事实 | 来源 | 等级 |
|---|---|---|---|
| 简体中文 | 《超越百岁：长寿的科学与艺术》（Outlive 中译），中译出版社 2024-01，定价 98 元，约 449–488 页；营销强调"全球销量超百万" | [中国青年报](https://news.qq.com/rain/a/20240115A0537E00)、[中图网](https://m.bookschina.com/9257666.htm)、[豆瓣书评](https://m.douban.com/book/review/15759705/) | B |
| 繁体中文（台湾） | 博客來畅销榜上：Attia《超預期壽命Ⅰ+Ⅱ》两册不分售（75 折 750 元）；Ramakrishnan《老化可以改變嗎？》；多本"抗老化 + 肌力训练"本土书和日本医生书（和田秀树等）的译本 | [博客來畅销榜（医疗保健）](https://www.books.com.tw/web/sys_saletopb/books/08)、[（生活风格）](https://www.books.com.tw/web/sys_saletopb/books/10) | B（快照） |
| 日本 | 2025 年出版市场 1.5462 万亿日元：纸书 5,939 亿日元（基本持平），非漫画电子书只有 459 亿日元（+1.5%） | [出版科学研究所，经 ORICON/Infoseek 报道](https://news.infoseek.co.jp/article/oricon_2432716/) | A（媒体转述） |
| 日本 | Sinclair《LIFESPAN 老いなき世界》（东洋经济新报社，2,640 日元含税）发售约 1 个月达 4 刷 5 万部，后超过 10 万部；主要读者为 40–50 多岁，也有不少 20–30 多岁 | [Book Bang 2020](https://www.bookbang.jp/article/647595)、[乐天](https://books.rakuten.co.jp/rb/16405480/) | B |

**解读**：
- **简体中文**：
  - 作者的中文稿本来就是源语言，制作成本最低。
  - 但市场上同类译作多以"长寿方法、健康法则"包装（例如"科学健康法则""百岁老人十项全能"）。本书若以"测量素养"为卖点，需要更强的问题式书名与案例开头。
  - 健康科普的合规表述与审读周期需要单列。
- **繁体中文**：
  - 是独立市场，不能只做简繁转换，用语要台湾化，例如"套件/軟體/資料"。
  - 台湾读者接受"两册不分售"的大部头，这对 33 章全本有利。
- **日本**：
  - 纸书为主，非漫画电子书市场很小，所以应优先出纸本。
  - 翻译版权通常经日本代理商授权给出版社。
  - LIFESPAN 的成绩说明日本读者接受大部头科学非虚构，但读者群与"人生 100 年时代"议题绑定，卷Ⅲ（住房、照护、自主）在日本可能比在美国更有吸引力。

---

## 2. 读者画像（按美加优先级排序）

| 代号 | 画像 | 现在读什么、买什么 | 他们的问题 | 本书对应章节 |
|---|---|---|---|---|
| **R1｜已测量的健康消费者**（核心） | 35–60 岁，受过高等教育；买过 Function、TruAge 之类检测，或戴 Oura/WHOOP；读过《Outlive》或《Super Agers》 | 长寿书、播客、检测报告 | "我的生物年龄比实际小 5 岁，这说明什么？""这个干预让我年轻了 3 岁，可信吗？" | 卷Ⅰ（1–9），第 18、20、25、29 章 |
| **R2｜面对患者提问的专业人士** | 基层医生、护士、药师、物理治疗师、教练、营养师 | 指南、《Why We Die》类书 | 怎样向患者解释检测报告和"逆龄"宣传，同时不夸大也不一概否定 | 第 4、5、18、29、31 章 |
| **R3｜科学型大众读者** | 读过《Why We Die》《Ageless》、Ed Yong 等作者的读者 | 科普非虚构 | 衰老科学到底知道什么、不知道什么 | 卷Ⅱ（10–22），第 32、33 章 |
| **R4｜照护者与政策读者**（次要，日本与台湾可能升为主要） | 照护年迈父母的中年人；地方健康和住房政策从业者 | 照护和老龄政策书 | 长寿和"值得过的生活"之间是什么关系；资源怎样分配 | 卷Ⅲ（23–30） |
| **R5｜学生与研究者**（配套） | 老年学、流行病学、生物统计学的学生与研究者 | 论文、教材 | 方法和可识别性 | PI/P3 论文、附录、可复核资产 |

**不作为目标读者**：
- 寻找具体补充剂、药物方案的读者；本书不提供个体处方，见 KERNEL。
- 想要"长生不老"叙事的读者。

明确写出这两点，可以减少差评中的"预期错配"。

---

## 3. 定位对结构与生产的影响（需作者裁决）

### 3.1 篇幅冲突（X147）

- DEC-011 的预算约为 33 万中文字（卷Ⅰ 9 万 + 卷Ⅱ 13.5 万 + 卷Ⅲ 10.5 万）。
- 按常用的经验换算（约 1 个中文字 ≈ 0.6–0.7 个英文词），**全译英文约 20–23 万词**。这个系数是经验值，未经来源核实，须由译者或编辑核对。
- 作为对照，篇幅很长的头部书《Outlive》英国平装版为 17 章、496 页（[TopDoctor 2026](https://topdoctormagazine.com/biohacking/outlive-science-art-longevity-paperback-review/)，C 级）。
- 一般经验是，美国大众非虚构的篇幅常在 8–12 万词之间。这也是经验值，须向代理或编辑确认。
- **结论**：33 章全本很难作为美国大众版直接出版。

**选项**：

| 选项 | 内容 | 优点 | 风险 |
|---|---|---|---|
| **M-A（建议）** 双版本 | 英文大众版约 10–13 万词，约 16–20 章，以卷Ⅰ为骨架，从卷Ⅱ/Ⅲ各选代表章；中文 33 章全本作为专著或学术版，并提供可复核的在线附录 | 适配美加的主战场；全本仍完整保存 | 两个版本要共享断言 ID，否则会分叉 |
| M-B 英文全本 | 33 章全部英文化，走大学出版社 | 不需删减 | 篇幅与价格都会限制大众渠道 |
| M-C 中文先行 | 先出中文全本，再出英文 | 生产最快 | 与"美加第一"的市场优先级相反 |

**建议采用 M-A**：
- 美加优先，意味着**英文大众版应直接用英文写作**，以中文全本为源，而不是逐句翻译。
- 共享 `CLAIM_LEDGER` 中的断言 ID，大众版每个数字都能追溯到台账。
- 这会新增一条"英文大众版章节映射"工作线，需要作者批准后才开工。本轮**未**改动 33 章地图。

### 3.2 格式与价格锚点（只作参考）

| 市场 | 观察到的锚点 | 来源 |
|---|---|---|
| 美国 | 精装新书约 28–30 美元；同类较早出版的电子书约 6–12 美元（《True Age》5.99 美元、《Jellyfish》11.99 美元，检索时价格） | [Kindle 页面](https://us.amazon.com/Ageless-Science-Getting-Older-Without-ebook/dp/B07X8D3D9X)；[kindleranker（C）](https://www.kindleranker.com/book_categories/11764645011/US/books+health,+fitness+&+dieting+aging+longevity) |
| 中国大陆 | 《超越百岁》定价 98 元 | 中图网（B） |
| 台湾 | 《超預期壽命Ⅰ+Ⅱ》75 折 750 元，原价约 1,000 元 | 博客來（B） |
| 日本 | 《LIFESPAN》2,640 日元含税 | Book Bang / 乐天（B） |

### 3.3 零售分类（待核）

- **Amazon**：Books › Health, Fitness & Dieting › Aging（节点 282840）；Kindle "Aging / Longevity"（节点 11764645011）。
- **BISAC**（**待用 BISG 官方表核对代码**）：
  - 主分类拟 HEALTH & FITNESS / Longevity；
  - 次分类拟 SCIENCE / Life Sciences / Biology，或 MEDICAL / Geriatrics；
  - 卷Ⅲ方向可加 SOCIAL SCIENCE / Gerontology。
  - 本轮未从 BISG 原表确认具体代码，因此不写代码。

### 3.4 书名检索（有限）

- 网页检索 "The Measures of Longevity" 没有找到同名图书。
- 相近的有：
  - 小说《The Measure》（Erlick 2022）；
  - Springer 人口学论文集《How Long Do We Live?》（书中使用"measures of longevity"这一术语）；
  - Cameron《The Longevity Book》。
- 这**不**证明书名唯一。出版前需要查美国国会图书馆、Bowker、USPTO 商标，以及目标市场的书目。
- **副题较长**。本文不建议改动，只提示代理或编辑可能对副题长度提出意见。

---

## 4. 合规与表述红线（营销文案同样适用）

1. 不承诺延寿、不提供个体处方；面向美国的文案注意 FTC 关于健康宣称的规则。
2. 不使用"首次""首个框架""填补空白"（沿用 X137）。
3. 引用检测公司的数据时注明"公司自报"。不与任何检测或补充剂公司做联合营销，以免出现利益冲突。
4. 批评竞品只针对方法，不针对人。

---

## 5. 下一轮研究（未完成）

| 序号 | 工作 | 目的 | 依赖 |
|---|---|---|---|
| MR-1 | 取得竞品的 BookScan 或 Nielsen 册数（通过代理或出版社） | 用真实数据替代 C 级估算 | 外部渠道 |
| MR-2 | 对 R1/R2 做 10–15 人访谈（已购检测者、基层医生） | 验证"测完之后怎么读数"这一需求 | 作者同意招募方式 |
| MR-3 | 对亚马逊 Aging 榜做 4–8 周的排名采样 | 区分常销书与新书冲榜 | 无 |
| MR-4 | 补充澳大利亚、新西兰、印度的数据，以及开卷（中国大陆）和 Oricon/日贩（日本）年度榜 | 补完优先级 2、3 的市场事实 | 无 |
| MR-5 | 用 BISG 官方表核对 BISAC 代码；完成 USPTO 与书目的书名检索 | 出版前合规 | 无 |
| MR-6 | 起草英文大众版章节映射（选项 M-A） | 需作者先批准 M-A | 作者裁决 |

---

## 附：本轮检索到但未采用的数据

- **"Outlive 上纽约时报榜超过 80 周"**：来源是博客，C 级，未核，不采用。
- **"Super Agers 月销售额约 50 万美元"**：来源是第三方估算，C 级，不采用。
- **全球图书市场规模、有声书年增长率等汇总**：来源是营销网站，C 级，不采用。
