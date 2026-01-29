/**
 * 阅读进度条和返回顶部按钮
 * 参考：https://blog.leonus.cn/2022/percent.html
 */

(function() {
    'use strict';

    // 创建进度条
    function createProgressBar() {
        const progressBar = document.createElement('div');
        progressBar.className = 'scroll-progress-bar';
        document.body.appendChild(progressBar);
        return progressBar;
    }

    // 创建返回顶部按钮
    function createBackToTop() {
        const backToTop = document.createElement('button');
        backToTop.className = 'back-to-top';
        backToTop.setAttribute('aria-label', '返回顶部');
        backToTop.innerHTML = `
            <span class="back-to-top-icon">↑</span>
            <span class="back-to-top-percent"><span class="percent-value">0</span>%</span>
        `;
        document.body.appendChild(backToTop);

        // 点击返回顶部
        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });

        return backToTop;
    }

    // 计算并更新进度
    function updateProgress(progressBar, backToTop) {
        const scrollTop = document.documentElement.scrollTop || window.pageYOffset;
        const windowHeight = document.documentElement.clientHeight;
        const documentHeight = Math.max(
            document.body.scrollHeight,
            document.documentElement.scrollHeight,
            document.body.offsetHeight,
            document.documentElement.offsetHeight,
            document.body.clientHeight,
            document.documentElement.clientHeight
        );

        // 计算滚动百分比
        const scrollPercent = Math.round((scrollTop / (documentHeight - windowHeight)) * 100);

        // 更新进度条宽度
        if (progressBar) {
            progressBar.style.width = scrollPercent + '%';
        }

        // 更新返回顶部按钮
        if (backToTop) {
            const percentValue = backToTop.querySelector('.percent-value');
            const icon = backToTop.querySelector('.back-to-top-icon');
            const percent = backToTop.querySelector('.back-to-top-percent');

            if (scrollPercent <= 95) {
                // 显示百分比
                if (icon) icon.style.display = 'none';
                if (percent) {
                    percent.style.display = 'inline-block';
                    if (percentValue) percentValue.textContent = scrollPercent;
                }
                backToTop.style.display = 'block';
            } else {
                // 显示箭头图标
                if (percent) percent.style.display = 'none';
                if (icon) icon.style.display = 'block';
                backToTop.style.display = 'block';
            }
        }
    }

    // 初始化
    function init() {
        const progressBar = createProgressBar();
        const backToTop = createBackToTop();

        // 初始更新
        updateProgress(progressBar, backToTop);

        // 监听滚动事件
        let ticking = false;
        window.addEventListener('scroll', function() {
            if (!ticking) {
                window.requestAnimationFrame(function() {
                    updateProgress(progressBar, backToTop);
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    // 页面加载完成后初始化
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
