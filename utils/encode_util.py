import os

encode_dict = {
    '.DV.': 'DolbyVision',
    ' DV ': 'Dolby Vision',
    'HDR': 'HDR',
    '10BIT': '10bit',
    'HEVC': 'HEVC',
    'BLURAY': 'BluRay',
    'BLU-RAY': 'BluRay'
}

def get_encode_in_name(name):
    name = name.upper()
    r = ''
    for x in encode_dict:
        if x in name:
            r = r + encode_dict[x]
    return r


if __name__ == '__main__':
    print(get_encode_in_name('Wong Fei Hung III Si wong jaang ba 1992 1080p USA Blu-ray AVC LPCM 2.0-KRUPPE    [免费] 剩余时间：22时55分'))
    # 批量测试
    folder = '/home/nate/data/极端试验样本/'
    for root, dirs, files in os.walk(folder):
        for x in files:
            print(f'{get_encode_in_name(x)} - {x}')