import os


def get_stream_in_name(name):
    file_full_name_up = name.upper()
    stream_file_name = [
        'CRUNCHYROLL', 'B-GLOBAL', 'BILIBILI', '.LINETV.', '[LINETV]', '.FRIDAY.',
        '[FRIDAY]', 'NETFLIX', '(LINETV', '(FRIDAY', '.BAHA.', ' BAHA ',
        '[BAHA]', 'SENTAI', '(BAHA', 'ABEMA', '(AT-X', '(BS11',
        '.VIU.', '[VIU]', '.CR.', ' CR ', '[CR]', '(BS4',
        '(TBS', ' NF ', '.NF.', 'KKTV', '(VIU', '(CR',
        '(MX', '(TX', '(NF', '(NF', 'WEBRIP', 'BDRIP',
        'WEBDL', 'REMUX', 'WEB'
    ]
    stream_output_name = [
        'CR', 'Bilibili', 'Bilibili', 'LINETV', 'LINETV', 'friDay',
        'friDay', 'Netflix', 'LINETV', 'friDay', 'Baha', 'Baha',
        'Baha', 'Sentai', 'Baha', 'Abema', 'AT-X', 'BS11',
        'Viu', 'Viu', 'CR', 'CR', 'CR', 'BS4',
        'TBS', 'Netflix', 'Netflix', 'KKTV', 'Viu', 'CR',
        'MX', 'TX', 'Netflix', 'Netflix', 'WebRip', 'BDRip',
        'WebDL', 'Remux','Web'
    ]
    for i in range(0, len(stream_file_name)):
        if stream_file_name[i] in file_full_name_up:
            return stream_output_name[i]
    return ''

if __name__ == '__main__':
    print(get_stream_in_name('【推しの子】 小鳥之翼 第二季 / Birdie Wing: Golf Girls Story S2 - 15 (CR 1920x1080 AVC AAC MKV)'))
    # 批量测试
    folder = '/home/nate/data/极端试验样本/'
    for root, dirs, files in os.walk(folder):
        for x in files:
            print(f'{get_stream_in_name(x)} - {x}')