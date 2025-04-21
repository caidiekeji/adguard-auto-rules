# 电视/流媒体广告拦截规则生成器

一个自动爬取并检测广告URL，生成AdBlock拦截规则的Python项目。

## 功能特点

- 🕷️ 基于Scrapy的爬虫，支持电视品牌、内容提供商和流媒体平台
- 🔍 使用已知广告域名列表检测广告URL
- 📝 自动生成AdGuard兼容的拦截规则
- ⚙️ 可配置的目标网站和广告域名
- 🔄 自动化GitHub Actions工作流

## 安装指南

1. 克隆本仓库
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

运行主脚本：
```bash
python main.py
```

执行流程：
1. 运行所有爬虫收集URL
2. 检测广告URL
3. 生成规则到`rules/adguard.txt`

## 配置说明

- 修改`config/target_sites.json`配置爬取目标
- 更新`ad_detector/known_ad_domains.txt`添加新的广告域名

## 参与贡献

1. Fork本仓库
2. 创建新分支开发功能
3. 提交Pull Request

## 开源协议

MIT开源协议
