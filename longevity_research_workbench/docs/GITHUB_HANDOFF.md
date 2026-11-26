# 手动建库交接 / Manual GitHub handoff

建议仓库名：`longevity-research-workbench`。建议**先Private**，版权/敏感性/作者和方法外审后再决定公开。当前没有创建远端，没有push，也没有设置分支规则、必需CI检查或真实reviewer。

## 1. 当前包包含与不包含

包含：本轮决策/书与论文研究提案、V6/V7两份正文快照、toolkit0.1.1候选及其上游历史说明、本轮测试与回执。

不包含：全部会话聊天、两第三方附件全文、旧v1–v6引擎全部文件、第三方大数据、旧ZIP/HTML。原本地历史仍完整保留；540文件hash核验仅证明其字节未变，不等540项全文人审。

如果希望“本SESSION全部历史”也进仓库，先建立分发清单：逐项审查 `corpus_engine_v1`–`v6` 与证据目录的许可、体积、敏感性；可加入 `archive/` 按版本保留，不执行旧prepare_bindings，不替换主工作台工具，不用同名目录造成多份活跃源。大数据只存DOI/受控访问说明和hash，必要时用外部数据归档或LFS；先审查再上传，不能先push后删（git历史仍在）。

## 2. 本地验证

在解压后的根目录：

```bash
python -m pip install -e ./methods/research-assurance
python tools/run_validation.py
```

第一条需要可用依赖源或本地wheel。验证脚本不联网、不访问附件、不要求原始历史路径；当前仓库软件结果不等新科学发现。

原始历史验收需要在本会话布局运行 `python tools/verify_history.py /home/user`；公开仓库解压到其他机器无法访问原540文件，不能把它当跨机器CI强制条件，也不能把missing当允许重设基线。

## 3. 在网页手动创建空仓库后（以下由你执行）

```bash
git init
git add .
git status --short
# 先人工检查待提交文件，确认没有凭据、保密数据或未授权材料
git commit -m "Initialize longevity research workbench and audited method candidate"
git branch -M main
# 复制你刚创建仓库的真实remote URL，执行 git remote add origin <真实URL>
# 确认无误后执行 git push -u origin main
```

没有把占位remote写入任何配置；不需要把token写入文件或告诉助手。

## 4. 发布前清单

- [ ] 确认书/论文作者与贡献，填写AI辅助披露；不把助手列为作者。
- [ ] 分开确定代码、原创文字、第三方资料的授权；当前没有擅自授予MIT/CC许可。
- [ ] 审查正文/历史日志中个人信息、私密路径、受控数据和受版权保护图表。
- [ ] 审核软件依赖、版本和许可证；按验证回执配置可重复环境。
- [ ] 先跑本地测试，再启用低权限普通pull_request CI；不得照搬附件高权限模板。
- [ ] 如启用branch protection/ruleset，人工设置审批人和必需检查；本地目录不能自动落实这些权限。
- [ ] 标记工程候选，不把软件测试成功当学术稿件ready；真实外审仍欠。

## 5. 未来拆仓条件

当第二个研究项目稳定复用、API/维护责任/许可明确，才把通用toolkit抽独立仓库和发布包。主书仓库固定版本引用，移除第二份活跃源码；历史版本保留快照或清楚归档，避免两边偷偷同步。
