# check_images.py
import requests

API_BASE = "https://fashion-radar2.vercel.app/api"

def check_missing_images():
    resp = requests.get(f"{API_BASE}/products")
    products = resp.json()
    
    missing = []
    for p in products:
        if not p.get("image_url") or p["image_url"] == "":
            missing.append({
                "brand": p.get("brand"),
                "name": p.get("name"),
                "url": p.get("url"),
            })
    
    print(f"總新品數：{len(products)}")
    print(f"缺少圖片：{len(missing)} 筆")
    for item in missing:
        print(f"  ❌ [{item['brand']}] {item['name']} → {item['url']}")

check_missing_images()
