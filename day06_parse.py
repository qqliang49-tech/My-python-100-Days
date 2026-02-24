from bs4 import BeautifulSoup
with open("douban.html","r",encoding="utf-8") as f:
    html_content = f.read()
soup = BeautifulSoup(html_content,"html.parser")
movies = soup.find_all("div",class_="item")
print(f"---成功发现{len(movies)}部电影---")
for movie in movies:
    title = movie.find("span",class_="title").text
    rating = movie.find("span",class_="rating_num").text
    print(f"🎬 电影:{title}| ⭐ 评分：{ rating}")
with open("movies_results.txt","w",encoding="utf-8") as f:
    for movie in movies:
        title = movie.find("span",class_="title").text
        rating = movie.find("span",class_="rating_num").text
        all_spans = movie.find_all("span")
        people_count = all_spans[-2].text.replace("人评价","")
        f.write(f"电影：{title} | 评分：{rating} | 评价人数{people_count}\n")
