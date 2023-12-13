import requests
response = requests.get(url="https://api.kanye.rest")
response.raise_for_status()
data = response.json()
quote = data['quote']
print(f"오늘의 격언: {quote}")