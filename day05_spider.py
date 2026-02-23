import requests

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("正在爬取豆瓣电影Top250...")

# 发送请求
response = requests.get(url, headers=headers)

# 逻辑判断
if response.status_code == 200:
    print("✅ 爬取成功！以下是部分内容预览：")
    print(response.text[:500])  # 只打印前500个字符预览
    
    with open("douban.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("💾 已将内容保存到 douban.html 文件中！")
else:
    print(f"❌ 抓取失败，错误代码：{response.status_code}")
