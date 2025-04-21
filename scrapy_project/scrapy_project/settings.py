import os
from pathlib import Path

BOT_NAME = 'scrapy_project'

# 动态获取项目根目录
project_root = Path(__file__).parent.parent.parent
config_path = project_root / 'config' / 'target_sites.json'

# 确保爬虫能找到配置文件
os.environ['TARGET_SITES_PATH'] = str(config_path)

SPIDER_MODULES = ['scrapy_project.spiders']
NEWSPIDER_MODULE = 'scrapy_project.spiders'

ROBOTSTXT_OBEY = True

FEED_FORMAT = 'json'
FEED_URI = '%(name)s.json'
FEED_EXPORT_ENCODING = 'utf-8'

# 启用日志输出到控制台
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'

USER_AGENT = 'Mozilla/5.0 (compatible; TVAdBlockBot/1.0; +https://github.com/yourusername/TV-AdBlock-Rules)'
