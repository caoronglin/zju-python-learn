#!/bin/bash
# 批量更新章节页面

echo "开始批量更新章节页面..."

# 提交当前更改
cd /home/crl/c/zju-python-learn
git add -A
git commit -m "更新章节：Python运算符优先级和结合性

- 添加完整的运算符优先级表格
- 详细说明结合性规则
- 提供实际应用示例
- 常见错误和陷阱说明
- 最佳实践建议

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin main

# 更新gh-pages
git checkout gh-pages
git merge main --no-edit
git push origin gh-pages
git checkout main

echo "✓ 更新完成并部署到GitHub Pages"
