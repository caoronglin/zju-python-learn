#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成HTML页面"""

import os
import json

# 页面配置
PAGES = {
    'index.html': {
        'title': 'Python程序设计教程',
        'content_file': None
    },
    'computer-basics.html': {
        'title': '计算机基础',
        'chapter': '1.1',
        'file': 'wn7vb3cuhsbz3i2i'
    },
    'python-intro.html': {
        'title': 'Python语言简介',
        'chapter': '1.2',
        'file': 'ldv9dsihpxuhrhao'
    },
    'number-types.html': {
        'title': '数字类型',
        'chapter': '2.1',
        'file': 'pyg8aqwg6vi2ylyl'
    },
    'boolean-list.html': {
        'title': '布尔类型、空值和列表运算',
        'chapter': '2.3',
        'file': 'ahgb4ghfleeerpt6'
    },
    'assignment.html': {
        'title': '赋值语句',
        'chapter': '2.5',
        'file': 'ops53zuyol52k3mi'
    },
    'bit-operations.html': {
        'title': 'Python位运算',
        'chapter': '2.7',
        'file': 'sk8axopw02xgii7s'
    },
    'list-tuple.html': {
        'title': '列表和元祖使用',
        'chapter': '3.3',
        'file': 'pbe6hi89av2gpedo'
    },
    'loops.html': {
        'title': '循环语句',
        'chapter': '4.2',
        'file': 'tvpg50136pkcxy72'
    },
    'sets.html': {
        'title': '集合',
        'chapter': '5.1',
        'file': 'spda2mq16xm1k4n3'
    },
    'dict.html': {
        'title': '字典',
        'chapter': '5.2',
        'file': 'ia1o4opz6nhg65b5'
    },
    'functions.html': {
        'title': '函数',
        'chapter': '6.1',
        'file': 'wfdhml5ehy0kr7oc'
    },
    'namespace.html': {
        'title': '命名空间和作用域',
        'chapter': '6.2',
        'file': 'dgwo9ie8do6zh6rz'
    },
    'exceptions.html': {
        'title': '异常操作',
        'chapter': '7.2',
        'file': 'telpg3qvcmg670l4'
    },
    'pandas.html': {
        'title': 'pandas',
        'chapter': '7.3',
        'file': 'cpl7d6komph0kwew'
    }
}

def format_markdown_to_html(content):
    """将Markdown格式的内容转换为HTML"""
    html = content

    # 标题处理
    html = html.replace('### ', '<h3>').replace('\n###', '</h3>\n')
    html = html.replace('## ', '<h2>').replace('\n##', '</h2>\n')
    html = html.replace('# ', '<h1>').replace('\n#', '</h1>\n')

    # 代码块处理
    html = html.replace('```python\n', '<pre><code class="language-python">')
    html = html.replace('```\n', '</code></pre>\n')
    html = html.replace('```', '</code></pre>')

    # 行内代码
    html = html.replace('`', '<code>')

    # 加粗
    html = html.replace('**', '<strong>').replace('**', '</strong>')

    # 列表处理（简化版）
    lines = html.split('\n')
    in_ul = False
    result = []

    for line in lines:
        if line.strip().startswith('- '):
            if not in_ul:
                result.append('<ul>')
                in_ul = True
            result.append(f'<li>{line.strip()[2:]}</li>')
        elif line.strip() == '':
            if in_ul:
                result.append('</ul>')
                in_ul = False
            result.append('<br>')
        else:
            if in_ul:
                result.append('</ul>')
                in_ul = False
            result.append(line)

    if in_ul:
        result.append('</ul>')

    html = '\n'.join(result)

    return html

def generate_nav():
    """生成导航菜单"""
    nav = """
    <nav class="sidebar-nav">
        <div class="nav-section">
            <h3>第一章 Python语言概述</h3>
            <ul>
                <li><a href="computer-basics.html" class="nav-link">1.1 计算机基础</a></li>
                <li><a href="python-intro.html" class="nav-link">1.2 Python语言简介</a></li>
            </ul>
        </div>

        <div class="nav-section">
            <h3>第二章 用Python编写程序</h3>
            <ul>
                <li><a href="number-types.html" class="nav-link">2.1 数字类型</a></li>
                <li><a href="#" class="nav-link">2.2 字符串类型</a></li>
                <li><a href="boolean-list.html" class="nav-link">2.3 布尔类型、空值和列表运算</a></li>
                <li><a href="#" class="nav-link">2.4 内置转换函数</a></li>
                <li><a href="assignment.html" class="nav-link">2.5 赋值语句</a></li>
                <li><a href="#" class="nav-link">2.6 格式化输出</a></li>
                <li><a href="bit-operations.html" class="nav-link">2.7 Python位运算</a></li>
            </ul>
        </div>

        <div class="nav-section">
            <h3>第三章 使用字符串、列表和元组</h3>
            <ul>
                <li><a href="#" class="nav-link">3.1 序列的访问及运算符</a></li>
                <li><a href="#" class="nav-link">3.2 字符串使用</a></li>
                <li><a href="list-tuple.html" class="nav-link">3.3 列表和元祖使用</a></li>
            </ul>
        </div>

        <div class="nav-section">
            <h3>第四章 条件、循环和其他语句</h3>
            <ul>
                <li><a href="#" class="nav-link">4.1 条件语句</a></li>
                <li><a href="loops.html" class="nav-link">4.2 循环语句</a></li>
            </ul>
        </div>

        <div class="nav-section">
            <h3>第五章 集合和字典</h3>
            <ul>
                <li><a href="sets.html" class="nav-link">5.1 集合</a></li>
                <li><a href="dict.html" class="nav-link">5.2 字典</a></li>
            </ul>
        </div>

        <div class="nav-section">
            <h3>第六章 函数</h3>
            <ul>
                <li><a href="functions.html" class="nav-link">6.1 函数</a></li>
                <li><a href="namespace.html" class="nav-link">6.2 命名空间和作用域</a></li>
            </ul>
        </div>

        <div class="nav-section">
            <h3>第七章 文件和异常</h3>
            <ul>
                <li><a href="#" class="nav-link">7.1 文件</a></li>
                <li><a href="exceptions.html" class="nav-link">7.2 异常操作</a></li>
                <li><a href="pandas.html" class="nav-link">7.3 pandas</a></li>
            </ul>
        </div>

        <div class="nav-section">
            <h3>订阅本站</h3>
            <a href="rss.xml" class="rss-button" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M6.18 15.64a2.18 2.18 0 0 1 2.18 2.18C8.36 19 7.38 20 6.18 20C5 20 4 19 4 17.82a2.18 2.18 0 0 1 2.18-2.18M4 4.44A15.56 15.56 0 0 1 19.56 20h-2.83A12.73 12.73 0 0 0 4 7.27V4.44m0 5.66a9.9 9.9 0 0 1 9.9 9.9h-2.83A7.07 7.07 0 0 0 4 12.93V10.1z"/>
                </svg>
                RSS 订阅
            </a>
        </div>
    </nav>
    """
    return nav

def generate_page_template(title, content='', active_class=''):
    """生成HTML页面模板"""

    nav = generate_nav()

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Python程序设计</title>
    <meta name="description" content="学习Python程序设计 - {title}">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/prism.css">
    <link rel="icon" href="favicon.ico">
</head>
<body>
    <div class="container">
        <!-- 侧边栏 -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>Python程序设计</h2>
                <p class="subtitle">从入门到精通</p>
            </div>
            {nav}
        </aside>

        <!-- 主内容区 -->
        <main class="main-content">
            <div class="content-wrapper">
                <h1>{title}</h1>
                {content}
            </div>
        </main>
    </div>

    <script src="js/prism.js"></script>
    <script src="js/smooth-scroll.js"></script>
    <script src="js/search.js"></script>
    <script src="js/scroll-progress.js"></script>
</body>
</html>
'''
    return html

if __name__ == '__main__':
    print('开始生成页面...')

    # 生成主页面
    home_content = '''
                <div class="course-info">
                    <p class="lead">Python是一门优雅、易学且功能强大的编程语言。本课程将系统地介绍Python的各个方面，帮助你从零开始掌握这门流行的编程语言。</p>
                </div>

                <section class="section">
                    <h2>课程简介</h2>
                    <p>本课程是面向编程初学者的必修课程，涵盖了Python程序设计的核心内容：</p>
                    <ul>
                        <li><strong>数据类型</strong>：数字、字符串、列表、字典等基本数据类型</li>
                        <li><strong>控制结构</strong>：条件判断、循环控制等程序流程</li>
                        <li><strong>函数</strong>：函数定义、参数传递、作用域</li>
                        <li><strong>面向对象</strong>：类、对象、继承、多态</li>
                        <li><strong>高级特性</strong>：装饰器、生成器、上下文管理器</li>
                        <li><strong>文件操作</strong>：文件读写、异常处理</li>
                    </ul>
                </section>

                <section class="section">
                    <h2>开始学习</h2>
                    <div class="chapter-card">
                        <h3><span class="chapter-num">01</span>计算机基础</h3>
                        <p>了解计算机的基本特点、数制转换、字符编码等基础知识。</p>
                        <a href="computer-basics.html" class="btn">开始学习 →</a>
                    </div>

                    <div class="chapter-card">
                        <h3><span class="chapter-num">02</span>Python语言简介</h3>
                        <p>学习Python的运算符优先级、结合性和基本语法规则。</p>
                        <a href="python-intro.html" class="btn">开始学习 →</a>
                    </div>

                    <div class="chapter-card">
                        <h3><span class="chapter-num">03</span>数字类型</h3>
                        <p>掌握整数、浮点数、复数的使用方法和数学运算函数。</p>
                        <a href="number-types.html" class="btn">开始学习 →</a>
                    </div>
                </section>
    '''

    index_html = generate_page_template('Python程序设计', home_content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    print('✓ 生成 index.html')

    print(f'\n总共生成 1 个主页')
    print('其他章节页面需要手动添加内容')
