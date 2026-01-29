#!/bin/bash

# 章节页面列表
declare -A pages=(
    ["python-intro.html"]="Python语言简介|1.2"
    ["number-types.html"]="数字类型|2.1"
    ["boolean-list.html"]="布尔类型、空值和列表运算|2.3"
    ["assignment.html"]="赋值语句|2.5"
    ["bit-operations.html"]="Python位运算|2.7"
    ["list-tuple.html"]="列表和元祖使用|3.3"
    ["loops.html"]="循环语句|4.2"
    ["sets.html"]="集合|5.1"
    ["dict.html"]="字典|5.2"
    ["functions.html"]="函数|6.1"
    ["namespace.html"]="命名空间和作用域|6.2"
    ["exceptions.html"]="异常操作|7.2"
    ["pandas.html"]="pandas|7.3"
)

echo "正在创建占位页面..."

for page in "${!pages[@]}"; do
    IFS='|' read -r title chapter <<< "${pages[$page]}"

    cat > "$page" << EOF
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} | Python程序设计</title>
    <meta name="description" content="学习Python程序设计 - ${title}">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/prism.css">
    <link rel="icon" href="favicon.ico">
</head>
<body>
    <div class="container">
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>Python程序设计</h2>
                <p class="subtitle">从入门到精通</p>
            </div>
            <nav class="sidebar-nav">
                <a href="index.html" class="back-to-home">← 返回首页</a>
            </nav>
        </aside>

        <main class="main-content">
            <div class="content-wrapper">
                <h1>${chapter} ${title}</h1>
                <div class="priority-badge">
                    <span class="star">📝</span>
                    <span class="text">本章节内容正在整理中，敬请期待...</span>
                </div>
                <section class="section">
                    <p>本章节将详细介绍<strong>${title}</strong>的相关知识点。</p>
                    <p>请先学习其他章节，完整内容即将上线。</p>
                </section>
            </div>
        </main>
    </div>

    <script src="js/prism.js"></script>
    <script src="js/smooth-scroll.js"></script>
    <script src="js/search.js"></script>
    <script src="js/scroll-progress.js"></script>
</body>
</html>
EOF
    echo "✓ 创建 $page"
done

echo ""
echo "所有占位页面创建完成！"
echo "您可以逐步添加详细内容。"
