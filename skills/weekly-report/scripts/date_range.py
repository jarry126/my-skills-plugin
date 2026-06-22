#!/usr/bin/env python3
"""计算本周的日期范围（周一到周日）。
被 weekly-report skill 调用，避免每次手动算日期。
"""
from datetime import date, timedelta


def week_range(today: date | None = None) -> tuple[date, date]:
    today = today or date.today()
    monday = today - timedelta(days=today.weekday())  # weekday(): 周一=0
    sunday = monday + timedelta(days=6)
    return monday, sunday


if __name__ == "__main__":
    start, end = week_range()
    print(f"{start.isoformat()} ~ {end.isoformat()}")
