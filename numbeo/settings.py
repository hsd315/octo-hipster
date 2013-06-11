# Scrapy settings for numbeo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'numbeo'

SPIDER_MODULES = ['numbeo.spiders']
NEWSPIDER_MODULE = 'numbeo.spiders'

ITEM_PIPELINES = ['numbeo.pipelines.NumbeoPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'numbeo (+http://www.yourdomain.com)'
