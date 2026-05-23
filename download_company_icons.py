import os
import urllib.request

icons = {
    "meta": "#0467DF",
    "amazon": "#FF9900",
    "nordstrom": "#000000",
}

os.makedirs("icons", exist_ok=True)

for slug, color in icons.items():
    url = f"https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/{slug}.svg"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg = response.read().decode('utf-8')
            svg = svg.replace('<svg ', f'<svg fill="{color}" ')
            with open(f"icons/{slug}.svg", "w") as f:
                f.write(svg)
        print(f"Downloaded {slug}.svg")
    except Exception as e:
        print(f"Error {slug}: {e}")
