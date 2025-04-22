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

# 更详细的日志设置
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# 下载设置
DOWNLOAD_TIMEOUT = 30
DOWNLOAD_DELAY = 2
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# 浏览器模拟
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

# 确保安装scrapy-user-agents包
