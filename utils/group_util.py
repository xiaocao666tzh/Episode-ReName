import os
import feedparser
import re
import time
try:
    from loguru import logger
except:
    # 兼容无loguru模块的环境，例如docker和群晖
    class logger:
        def info(s):
            print(f'| INFO     | {s}')

        def warning(s):
            print(f'| WARNING  | {s}')

def get_nc_name():
    # 获取 NC_Raws 组名
    nc_name = ''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    nc_txt_path = current_dir + '/nc_raws_auto.txt'
    with open(nc_txt_path, 'r') as f:
        nc_txt = f.read()
        try:
            nc_name_local, lasttime = nc_txt.split('\n')
            lasttime = int(lasttime)
            print(nc_txt, nc_name_local, lasttime)
            if time.time() - lasttime <= 300:
                nc_name = nc_name_local
                return nc_name
        except:
            pass
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
        with open(nc_txt_path, 'w') as f:
            f.write(nc_name + '\n' + str(int(time.time())))
    return nc_name


nc_name = get_nc_name()
logger.info(f'NC-Raws组名为{nc_name}')


group_dict = {'Nekomoe kissaten': '喵萌',
              'BeanSub': '豌豆',
              'FZSD': '风之圣殿',
              nc_name: 'NC-Raws',
              'Sakurato': '桜都',
              'SBSUB': '银色子弹',
              'Airota': '千夏',
              'DMG': '动漫国',
              'UHA-WINGS': '悠哈璃羽',
              'XKSub': '星空',
              'orion origin': '猎户',
              'KissSub': '爱恋',
              'KTXP': '极影',
              'Suzu-Kaze': '铃风',
              'WMSUB': '风车',
              'Skymoon-Raws': '天月'}


def get_group_in_name(name):
    if os.path.isabs(name):
        name = os.path.basename(name)
        name = os.path.splitext(name)[-1]
        logger.info(f'获取group，name为{name}')
    # 适配 0day 命名方式资源
    if name.find('[') == 0:
        group = name.split("[")[1].split("]")[0]
        regex = re.compile('|'.join(map(re.escape, group_dict)))
        group = regex.sub(lambda match: group_dict[match.group(0)], group)
        return group
    elif name.find('【') == 0:
        group = name.split("【")[1].split("】")[0]
        regex = re.compile('|'.join(map(re.escape, group_dict)))
        group = regex.sub(lambda match: group_dict[match.group(0)], group)
        logger.info(f'获取到的组名为{group}')
        return group
    # 适配PT命名方式
    try:
        group = name[-15:]
    except:
        group = name
    if group.rfind('@') != -1:
        group = group[int(group.rfind('@'))+1:]
        return group
    elif group.rfind('-') != -1:
        group = group[int(group.rfind('-'))+1:]
        return group
    else:
        return ''


if __name__ == '__main__':
    print(get_group_in_name("D:\Software\Documents\GitHub\Episode-ReName/test\s01/Ars no Kyojuu S01E01-[1080p][BDRIP][x265.FLAC].mkv"))
    # 批量测试
    folder = '/home/nate/data/极端试验样本/'
    for root, dirs, files in os.walk(folder):
        for x in files:
            print(f'{get_group_in_name(x)} - {x}')
