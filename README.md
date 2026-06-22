# my-skills-plugin

个人效率技能合集。

## 包含的 skill
- **weekly-report** —— 把零散工作整理成结构统一的周报，支持 team/boss/brief 三种风格。

## 目录结构
```
my-skills-plugin/
├── .claude-plugin/
│   └── plugin.json          # 插件清单
├── skills/
│   └── weekly-report/       # 一个 skill（格式和单独使用时完全一样）
│       ├── SKILL.md
│       ├── scripts/date_range.py
│       └── references/styles.md
└── README.md
```

## 本地安装测试
把整个 my-skills-plugin 文件夹放到任意位置，在 Claude Code 里：
```
/plugin marketplace add /本地路径/到/包含这个插件的市场仓库
/plugin install my-skills-plugin@<市场名>
```
（需要先有一个 marketplace 来承载它，见下方 marketplace.json 示例。）
