BOT_NAME = "steam_tags"

SPIDER_MODULES = ["steam_tags.spiders"]
NEWSPIDER_MODULE = "steam_tags.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
