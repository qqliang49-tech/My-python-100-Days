import requests
from bs4 import BeautifulSoup
import time
with open("movies_results.txt","w",encoding="utf-8") as f:
    for i in range(0,250,25):
        url = f"https://movie.douban.com/top250?start={i}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWekit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }
        print(f"正在爬取第{i//25+1}页数据...")
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            movies = soup.find_all("div", class_="item")
            for movie in movies:
                title_tag = movie.find("span",class_="title")
                rating_tag = movie.find("span",class_="rating_num")
                if title_tag and rating_tag:
                    title = title_tag.text
                    rating = rating_tag.text
                else:
                    title = "未知电影"
                    rating = "未知评分"
                spans = movie.find_all("span")
                if len(spans) >=2: 
                    people_count = spans[-2].text.replace("人评价","")
                else:
                    people_count = "未知"
                f.write(f"电影：{title} | 评分：{rating} | 评价人数{people_count}\n")
            time.sleep(1)
        except Exception as e:
            print(f"第{i//25 + 1}页爬取出现意外：{e}")    
print("恭喜！250部电影已经全部入库！")    
