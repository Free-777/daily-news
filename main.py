导入 requests
导入 datetime

print("⏳ 正在获取今日热门新闻（Hacker News Top 10）...")

# 获取新闻
尝试:
    top_ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10).json()[:10]
    news_list = []
对于 idx, nid 在 top_ids, )中：
        data = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{nid}.json", timeout=5).json()
        title = data.get('title', '无标题')
        url = data.get('url', f"https://news.ycombinator.com/item?id={nid}")
        新闻列表。追加(f"{索引}. {标题}\n   链接: {网址}")
    内容 = "\n\n".拼接(新闻列表)
except Exception as e:
    content = f"抓取失败: {e}"

# 打印到日志（你可以在Actions运行记录里看到）
print("\n" + "="*50)
(f" 新闻推送 - {datetime.date.today()}")
打印("="*50)
print(content)
打印
