# my-skills-plugin

个人效率与 AI 工作流技能合集。

## 包含的 skill
- **weekly-report** —— 把零散工作整理成结构统一的周报，支持 team/boss/brief 三种风格。
- **clarify-before-execute** —— 在执行复杂任务前先澄清真实目标、边界、约束和验收标准。
- **prd-to-acceptance** —— 将 PRD、原型和业务规则转换为 MVP 范围、验收矩阵和证据契约。
- **pause-and-handoff** —— 暂停任务时生成可供其他 AI 工具继续执行的 Markdown 交接文档。

## 目录结构
```
my-skills-plugin/
├── .claude-plugin/
│   └── plugin.json          # 插件清单
├── skills/
│   ├── weekly-report/
│   ├── clarify-before-execute/
│   ├── prd-to-acceptance/
│   └── pause-and-handoff/
├── docs/
│   └── privacy-audit.md
└── README.md
```

## 隐私与脱敏

本仓库只发布通用 skills 和模板，不包含内部项目代码、公司 PRD、真实业务规则、截图、日志、账号密码或个人敏感数据。

发布审计见 `docs/privacy-audit.md`。

## 本地安装测试
把整个 my-skills-plugin 文件夹放到任意位置，在 Claude Code 里：
```
/plugin marketplace add /本地路径/到/包含这个插件的市场仓库
/plugin install my-skills-plugin@<市场名>
```
（需要先有一个 marketplace 来承载它，见下方 marketplace.json 示例。）
