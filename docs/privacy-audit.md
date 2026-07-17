# Privacy Audit

审计时间：2026-07-17

## 审计范围

本次开源候选仓库仅包含：

- `skills/clarify-before-execute`
- `skills/prd-to-acceptance`
- `skills/pause-and-handoff`
- 通用 README、LICENSE、贡献说明、安装脚本和本审计文档

明确排除：

- 任何内部项目代码
- 任何公司 PRD、原型、业务规则、接口文档
- 任何验收报告、截图、运行日志、数据库数据
- 任何本地路径、账号密码、手机号、身份证号或测试用户数据

## 已知风险处理

源项目是基于公司真实需求构建的内部项目，不适合直接开源，也不应作为本仓库的一部分发布。

本仓库只复用从项目过程中沉淀出的通用工作流方法，不复用具体业务材料。

## 本地扫描命令

发布前应执行：

```bash
rg -n --hidden "(password|passwd|pwd|secret|token|cookie|本地绝对路径|公司内部项目名|真实姓名|真实证件号|真实手机号)" .
```

预期结果：

```text
仅允许命中 docs/privacy-audit.md 中用于说明审计规则的敏感词列表。
```

## 发布门槛

- `git status --short` 中只包含本仓库预期文件。
- 敏感词扫描无代码或 skill 内容命中。
- 不包含源项目历史，不从内部项目目录初始化 Git 历史。
- GitHub 仓库公开前再次确认远程地址和仓库名。
