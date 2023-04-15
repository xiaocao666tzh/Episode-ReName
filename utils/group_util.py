import os
import feedparser

def get_nc_name():
    # 获取 NC_Raws 组名
    nc_rss_url = ['https://ouo.si/feed?page=rss', 'https://ouo.si/feed?page=rss', 'https://acg.rip/user/5570.xml', 'https://bangumi.moe/rss/tags/63e4b7585fa12c0007949b88', 'https://share.acgnx.se/rss-user-529.xml']
    for i in range(0,len(nc_rss_url)):
        feed = feedparser.parse(nc_rss_url[i])
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
    return nc_name

nc_name = get_nc_name()

group_list = ['Lilith-Raws', '[Ani]', 'SubsPlease', 'Ohys-Raws', '喵萌', 'LoliHouse', '豌豆', '桜都', '7³ACG', '银色子弹', 'SweetSub', '千夏', '动漫国', 'VCB', '悠哈璃羽']

if nc_name != None:
    group_list.append(nc_name)

def get_group_in_name(name):
    for i in group_list:
        if i in name:
            if i == nc_name:
                return 'NC-Raws'
            if name.find('[') == 0:
                group = name.split("[")[1].split("]")[0]
                if i in group:
                    return group
            elif name.find('【') == 0:
                group = name.split("【")[1].split("】")[0]
                if i in group:
                    return group
            else:
                return i

if __name__ == '__main__':
    print(get_group_in_name("【推しの子】 我內心的糟糕念頭 / Boku no Kokoro no Yabai Yatsu - 03 (Sentai 1920x1080 AVC AAC MKV)"))
    # 批量测试
    folder = '/home/nate/data/极端试验样本/'
    for root, dirs, files in os.walk(folder):
        for x in files:
            print(f'{get_group_in_name(x)} - {x}')