"""
 故宫壁纸
 版本: v1.8
 作者: kingc2022
 代码编辑器: Microsoft Visual Studio Code
 文档&注释生成: Mintlify Doc Writer for Python, JavaScript, TypeScript, C++, PHP, Java, C#, Ruby & more
 程序用到的库:
  · requests
  · re
  · os
  · datetime
  · time

 License: https://github.com/kingc2022/GuGongWallpaper/blob/main/LICENSE
 Github: https://github.com/kingc2022
 Github项目地址: https://github.com/kingc2022/GuGongWallpaper
 --------------------
 Wallpaper of the imperial palace
 Version: v1.8
 Author: kingc2022
 Code editor: Microsoft Visual Studio Code
 Documentation & comment generation: Mintlify Doc Writer for Python, JavaScript, TypeScript, C++, PHP, Java, C#, Ruby & more
 Library used by the program:
   · requests
   · re
   · os
   · datetime
   · time

 License: https://github.com/kingc2022/GuGongWallpaper/blob/main/LICENSE
 Github: https://github.com/kingc2022
 Making project address: https://github.com/kingc2022/GuGongWallpaper
"""
# 导入程序运行所需的库。
import requests
import re
import os
from datetime import datetime
import time

def main(page):
    """
    它从网站下载图像。
    
    :param page: 您要抓取的页面数
    """
    # 保存图片的名称
    pic_name = "0"
    # 翻页的for循环
    for i in range(1,page):
        # 爬虫的 headers
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'secure; acw_tc=b65cfd3716542646761064945e6b2e3f38ecdf13260981a1a809d960fa1afd; PHPSESSID=66a068a5b68beeb567eeb602a805272e; saw_terminal=default; UM_distinctid=18129dbb8c821a-088ba05f77c4f8-9126f2c-15f900-18129dbb8c9157; CNZZDATA1261553859=1879722444-1654263813-%7C1654263813; _abfpc=927f5ff44ead9af71b6ad7e5cd811d19dc9cfbf7_2.0; secure; cna=fccf890f80c665a90a7d9ad66ed40b13; cn_1261553859_dplus=%7B%22distinct_id%22%3A%20%2218129dbb8c821a-088ba05f77c4f8-9126f2c-15f900-18129dbb8c9157%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201654264687%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201654264687%2C%22initial_view_time%22%3A%20%221654263813%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        url = f"https://www.dpm.org.cn/lights/royal/p/{i}.html"
        base_url = "https://www.dpm.org.cn"
        big_img_base_url = "https://img.dpm.org.cn"
        save_path = "D:/Desktop/imgs"

        print(f"正在爬取第{str(i)}页:\n")

        response = requests.get(url,headers=headers)
        response.encoding = response.apparent_encoding
        code = response.text
        a_tag = re.compile('<a target="_blank" href="/light/(\d+).html"><img alt=".*?" title=".*?" src="https://img.dpm.org.cn/Uploads/Picture/.*?"></a>',re.S)
        pic_ids = re.findall(a_tag,code)

        # 图片详细页面的for循环
        for j in range(len(pic_ids)):
            pic_url = f"{base_url}/light/{pic_ids[j]}"
            # 爬虫的 headers
            h = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Cookie': 'secure; acw_tc=b65cfd3716542646761064945e6b2e3f38ecdf13260981a1a809d960fa1afd; PHPSESSID=66a068a5b68beeb567eeb602a805272e; saw_terminal=default; UM_distinctid=18129dbb8c821a-088ba05f77c4f8-9126f2c-15f900-18129dbb8c9157; CNZZDATA1261553859=1879722444-1654263813-%7C1654263813; _abfpc=927f5ff44ead9af71b6ad7e5cd811d19dc9cfbf7_2.0; cna=fccf890f80c665a90a7d9ad66ed40b13; Secure; cn_1261553859_dplus=%7B%22distinct_id%22%3A%20%2218129dbb8c821a-088ba05f77c4f8-9126f2c-15f900-18129dbb8c9157%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201654265359%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201654265359%2C%22initial_view_time%22%3A%20%221654263813%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D',
                'Pragma': 'no-cache',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }
            print(f"\t正在爬取第{str(j+1)}张壁纸")
            res = requests.get(pic_url,headers=h)
            res.encoding = res.apparent_encoding
            sc = res.text
            regular = re.compile('<img style="visibility: visible;width: 100%;" src="(.*?)">',re.S)
            big_img_url = re.findall(regular,sc)

            # 原始图片1920X1080的for循环
            for k in range(len(big_img_url)):
                big_img_url[k] = big_img_url[k].replace('" />\r\n    <div class="hide_wall','')
                r = requests.get(f"{big_img_base_url}{big_img_url[k]}")
                content = r.content
                if os.path.exists(save_path):
                    print(f"\t正在保存第{str(j+1)}张壁纸\n")
                    with open(f"{save_path}/{str(int(pic_name)+1)}.jpg","wb") as f:
                            f.write(content)
                    pic_name = str(int(pic_name)+1)
                else:
                    raise ValueError("你输入的路径不存在!")

if __name__ == "__main__":
    page = int(input("共124页, 每页9张, 爬取几页?\n"))
    page = page + 1
    start = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    start_time = time.time()
    main(page)
    end = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    end_time = time.time()
    time_diff = end_time-start_time
    print("爬取&保存成功!\n")
    print(f"开始时间: {start}\n结束时间: {end}")
    hours = time_diff // 3600
    minutes = time_diff // 60
    hours = int(hours)
    minutes = int(minutes)
    seconds = time_diff - hours*3600 - minutes*60
    seconds = int(seconds)
    print(f"共{hours}小时{minutes}分钟{seconds}秒")