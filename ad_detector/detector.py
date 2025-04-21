import re
from urllib.parse import urlparse

class AdDetector:
    def __init__(self):
        # 从文件加载已知广告域名
        with open('ad_detector/known_ad_domains.txt', 'r') as f:
            self.known_ad_domains = [line.strip() for line in f if line.strip()]
        
        self.ad_keywords = [
            'ad', 'ads', 'adserver', 'advert', 'doubleclick',
            'googleads', 'tracking', 'analytics', 'pubads',
            'adservice', 'adsystem', 'adnxs', 'adtech',
            'amazon-adsystem', 'scorecardresearch'
        ]
    
    def is_ad_url(self, url):
        try:
            domain = urlparse(url).netloc
            if not domain:
                return False
                
            # 检查已知广告域名
            if domain in self.known_ad_domains:
                return True
                
            # 检查域名中的广告关键词
            domain_parts = domain.split('.')
            for part in domain_parts:
                if part in self.ad_keywords:
                    return True
                    
            # 检查路径中的广告关键词
            path = urlparse(url).path.lower()
            for keyword in self.ad_keywords:
                if keyword in path:
                    return True
                    
            return False
        except Exception as e:
            print(f"Error checking URL {url}: {str(e)}")
            return False
