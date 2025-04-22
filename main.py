import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ad_detector.detector import AdDetector
import os
import sys
from datetime import datetime
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def run_spiders():
    # 获取项目根目录并设置路径
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)  # 确保工作目录正确
    
    # 设置环境变量
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'scrapy_project.scrapy_project.settings'
    
    # 调试日志
    logging.info(f"Project root: {project_root}")
    logging.info(f"Current working directory: {os.getcwd()}")
    logging.info(f"Config path: {os.path.join(project_root, 'config', 'target_sites.json')}")
    
    # 添加必要的路径到sys.path
    sys.path.insert(0, project_root)
    scrapy_project_path = os.path.join(project_root, 'scrapy_project')
    sys.path.insert(0, scrapy_project_path)
    
    process = CrawlerProcess(get_project_settings())
    
    spiders = [
        'tv_brands',
        'content_providers',
        'streaming_platforms'
    ]
    logging.info(f"Starting spiders: {spiders}")
    
    for spider in spiders:
        logging.info(f"Starting spider: {spider}")
        process.crawl(spider)
    
    process.start()
    
    # 合并结果
    all_urls = []
    for spider in spiders:
        try:
            with open(f'{spider}.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                all_urls.extend(data)
            os.remove(f'{spider}.json')
            logging.info(f"Collected {len(data)} URLs from {spider}")
        except FileNotFoundError:
            logging.warning(f"No data found for spider: {spider}")
            continue
    
    logging.info(f"Total URLs collected: {len(all_urls)}")
    return all_urls

def generate_rules(urls):
    detector = AdDetector()
    rules = set()
    
    for item in urls:
        if detector.is_ad_url(item['url']):
            domain = item['domain']
            if domain:
                rule = f"||{domain}^"
                rules.add(rule)
    
    return sorted(rules)

def save_rules(rules):
    if not os.path.exists('rules'):
        os.makedirs('rules')
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('rules/adguard.txt', 'w', encoding='utf-8') as f:
        f.write(f"! Title: Comprehensive TV/Streaming AdBlock Rules\n")
        f.write(f"! Description: Blocks ads on TV brands, content providers and streaming platforms\n")
        f.write(f"! Version: 1.0\n")
        f.write(f"! Last updated: {timestamp}\n")
        f.write(f"! Expires: 1 day (update frequency)\n")
        f.write(f"! Homepage: https://github.com/yourusername/TV-AdBlock-Rules\n")
        f.write(f"! License: MIT\n\n")
        f.write("\n".join(rules))
        f.write("\n")
    
    logging.info(f"Saved {len(rules)} rules to rules/adguard.txt")

if __name__ == "__main__":
    setup_logging()
    try:
        logging.info("Starting spider...")
        urls = run_spiders()
        
        logging.info("Generating rules...")
        rules = generate_rules(urls)
        
        logging.info("Saving rules...")
        save_rules(rules)
        logging.info("Done!")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)
