import requests

response = requests.post(
    "https://libretranslate.de/translate",
    headers={"Content-Type": "application/json"},
    json={
        "q": "من دانشجوی دانشگاه وین هستم.",
        "source": "fa",
        "target": "en",
        "format": "text"
    }
)

print(response.json())
