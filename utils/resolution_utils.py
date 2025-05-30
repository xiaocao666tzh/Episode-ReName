import os

# 分辨率工具

resolution_dict = {
    # 分辨率
    # https://www.displayninja.com/720p-vs-1080p-vs-1440p-vs-4k-vs-8k/
    '8192x4320': '4320p',
    '7680x4320': '4320p',
    '6144x3160': '3160p',
    '5120x2700': '2700p',
    '3840x2160': '2160p',
    '2048x1080': '1440p',
    '1920x1080': '1080p',
    '1280x720': '720p',
    # p
    '4320p': '4320p',
    '2160p': '2160p',
    '1440p': '1440p',
    '1080p': '1080p',
    '720p': '720p',
    '480p': '480p',
    '360p': '360p',
    '240p': '240p',
    '144p': '144p',
    # k
    '4k': '2160p',
    '8k': '4320p',
    '16k': '8640p',
}


def get_resolution_in_name(name):
    name = name.lower()
    for x in resolution_dict:
        if x in name:
            return resolution_dict[x]
    return ''


if __name__ == '__main__':
    print(get_resolution_in_name('aaa 1920X1080.mp4'))
    # 批量测试
    folder = '/home/nate/data/极端试验样本/'
    for root, dirs, files in os.walk(folder):
        for x in files:
            print(f'{get_resolution_in_name(x)} - {x}')
