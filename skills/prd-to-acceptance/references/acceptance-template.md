# 验收基线模板

## 范围契约

| ID | 需求 | 优先级 | 本期结论 | 理由 | 依赖 |
|---|---|---|---|---|---|
| SCOPE-001 | 示例核心能力 | P0 | 实现 | 构成核心业务闭环 | 无 |
| SCOPE-002 | 示例外部授权 | OUT | 暂不实现 | 当前缺少正式账号 | 正式账号 |

## 行为验收矩阵

| ID | 等级 | 业务目标 | 前置条件与操作 | UI 结果 | 接口结果 | 数据结果 | 负向场景 | 验收方式 | 证据 |
|---|---|---|---|---|---|---|---|---|---|
| DEMO-001 | P0 | 用户完成核心操作 | 已登录并提交合法数据 | 显示成功状态 | HTTP 200 且业务成功 | 仅新增一条记录 | 重复提交不重复创建 | 集成测试+UI | 报告与截图 |

## 机器可读规则示例

```yaml
project: example
result_levels:
  - PASS
  - PARTIAL_PASS
  - BLOCKED
  - FAIL

rules:
  - id: DEMO-001
    severity: P0
    goal: 用户完成核心操作
    preconditions:
      - 已建立测试会话
    actions:
      - 提交合法数据
    expect:
      ui:
        success_state_visible: true
      api:
        http_status: 200
        success: true
      database:
        created_rows: 1
        duplicate_rows: 0
    evidence:
      - integration_test
      - ui_screenshot
```

## 证据契约

| 层级 | PASS 条件 | 证据位置 |
|---|---|---|
| 构建 | 前后端构建退出码为 0 | 构建日志 |
| 业务 | P0 正向和负向场景全部通过 | 测试报告 |
| 数据 | 迁移版本和核心表断言正确 | 数据库检查日志 |
| UI | 核心操作可达且状态反馈正确 | UI 日志与截图 |
| 运行 | 无未解释的严重错误 | 日志扫描报告 |
