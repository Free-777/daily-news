import requests
import datetime
import time

print("⏳ 正在获取今日热门新闻（Hacker News Top 10）...")

def fetch_with_retry(url, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url, timeout=15)
            return response
        except Exception as e:
            print(f"Warning: attempt {i+1} failed: {e}")
            time.sleep(2)
    raise Exception(f"All retries failed for: {url}")

try:
    response = fetch_with_retry("https://hacker-news.firebaseio.com/v0/topstories.json")
    top_ids = response.json()[:10]
    
    news_list = []
    for idx, nid in enumerate(top_ids, 1):
        try:
            data = fetch_with_retry(f"https://hacker-news.firebaseio.com/v0/item/{nid}.json").json()
            title = data.get('title', 'No Title')
            url = data.get('url', f"https://news.ycombinator.com/item?id={nid}")
            news_list.append(f"{idx}. {title}\n   Link: {url}")
        except Exception as e:
            news_list.append(f"{idx}. Failed to fetch this item: {e}")
    
    content = "\n\n".join(news_list)
    print("Successfully fetched news!")

except Exception as e:
    content = f"Failed to fetch: {e}"
    print(content)

print("\n" + "="*50)
print(f"News Push - {datetime.date.today()}")
print("="*50)
print(content)
print("="*50)
