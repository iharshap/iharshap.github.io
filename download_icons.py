import os
import urllib.request

icons = {
    "powerbi": "#F2C811",
    "databricks": "#FF3621",
    "presto": "#000000",
    "apachehive": "#FDEE21",
    "teradata": "#F37440",
    "awslambda": "#FF9900"
}

os.makedirs("icons", exist_ok=True)

for slug, color in icons.items():
    url = f"https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/{slug}.svg"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg = response.read().decode('utf-8')
            # insert fill attribute
            svg = svg.replace('<svg ', f'<svg fill="{color}" ')
            with open(f"icons/{slug}.svg", "w") as f:
                f.write(svg)
        print(f"Downloaded {slug}.svg")
    except Exception as e:
        print(f"Error {slug}: {e}")
