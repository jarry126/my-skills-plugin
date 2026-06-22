# weekly-report skill

把零散工作内容整理成结构统一的周报，支持 team / boss / brief 三种风格。

## 目录结构
```
weekly-report/
├── SKILL.md              # 核心：何时触发 + 步骤 + 基础格式
├── scripts/
│   └── date_range.py     # 计算本周日期范围（周一~周日）
└── references/
    └── styles.md         # 三种周报风格的详细规则（按需读取）
```

## 安装（Claude Code）
把整个 weekly-report 文件夹放到：
```
~/.claude/skills/weekly-report/
```
然后重启 Claude Code。

## 测试
```
帮我写个周报：这周做完了登录页改版，修了3个bug，下周要做支付模块，用boss风格
```
预期：Claude 会调用 date_range.py 填日期，按 boss 风格输出。

## 这个 skill 演示了什么
- frontmatter 里 description 怎么写触发词
- 正文如何"指路"到 scripts/ 和 references/
- 渐进式加载：平时只看 description，触发后读正文，需要时才读 references
```
