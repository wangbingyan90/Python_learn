from multiprocessing.pool import Pool

class Menu:
    def __init__(self):
        self.title = '网易云音乐'



if __name__ == '__main__':
    select = ['1,爬取热门歌单','2,爬取歌单详细','3,爬取歌曲评论']
    while True:
        for s in select:
            print(s)
        key = input("选择操作:")
        
        # 爬取歌单
        if key == '1':

            