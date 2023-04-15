import os


def get_stream(name):
    file_full_name_up = name.upper()
    stream_file_name = ['.BAHA.', ' BAHA ', '[BAHA]', '(BAHA', '.CR.', ' CR ', '[CR]', '(CR', 'CRUNCHYROLL', 'B-GLOBAL',
                        'BILIBILI', 'ABEMA', '(AT-X', '(BS11', '(BS4', '(TBS', '(MX', '(TX', 'NETFLIX', ' NF ', '(NF',
                        '.NF.', '(NF', 'KKTV', 'WEBRIP', 'BDRIP', 'WEB']
    stream_output_name = ['Baha', 'Baha', 'Baha', 'Baha', 'CR', 'CR', 'CR', 'CR', 'CR', 'Bilibili', 'Bilibili', 'Abema',
                          'AT-X', 'BS11', 'BS4', 'TBS', 'MX', 'TX', 'Netflix', 'Netflix', 'Netflix', 'Netflix',
                          'Netflix', 'KKTV', 'WebRip', 'BDRip', 'Web']
    for i in range(0, len(stream_file_name)):
        if stream_file_name[i] in file_full_name_up:
            return stream_output_name[i]
    return 'None'

if __name__ == '__main__':
    print(get_stream('【推しの子】 小鳥之翼 第二季 / Birdie Wing: Golf Girls Story S2 - 15 (CR 1920x1080 AVC AAC MKV)'))
    # 批量测试
    folder = '/home/nate/data/极端试验样本/'
    for root, dirs, files in os.walk(folder):
        for x in files:
            print(f'{get_stream(x)} - {x}')