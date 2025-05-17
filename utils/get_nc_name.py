import feedparser
import time

nc_rss_url = ['https://ouo.si/feed?page=rss', 'https://ouo.si/feed?page=rss', 'https://acg.rip/user/5570.xml', 'https://bangumi.moe/rss/tags/63e4b7585fa12c0007949b88', 'https://share.acgnx.se/rss-user-529.xml']
for i in range(0, len(nc_rss_url)):
    try:
        feed = feedparser.parse(nc_rss_url[i])
    except:
        continue
    try:
        first_item_title = feed.entries[0].title
    except IndexError:
        continue
    nc_name = ''
    try:
        nc_name = first_item_title.split("[")[1].split("]")[0]
        print(nc_name)
    except:
        try:
            nc_name = first_item_title.split("【")[1].split("】")[0]
        except:
            nc_name = first_item_title[:4]
    if nc_name != '':
        break
if nc_name == '':
    nc_name = None
else:
    with open('nc_raws_auto.txt', 'w', encoding='utf-8') as f:
        f.write(nc_name + '\n' + str(int(time.time())))