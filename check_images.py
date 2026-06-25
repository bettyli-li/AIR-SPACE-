# check_images.py
import requests

# 提示：若依然報錯，這行網址高機率需要小潔主管給妳實際有帶 Token 密碼的網址喔！
API_BASE = "https://fashion-radar2.vercel.app/api"

def check_missing_images():
    try:
        print(f"正在連線至系統 API 進行檢查：{API_BASE}/products ...")
        resp = requests.get(f"{API_BASE}/products")
        
        # 【防撞安全氣囊 1】：如果網頁狀態不是 200 (成功)，直接報錯
        resp.raise_for_status() 
        
        # 【防撞安全氣囊 2】：檢查回傳的是不是文字而不是商品清單
        try:
            products = resp.json()
        except ValueError:
            print(f"❌ 錯誤：網址連上了，但回傳的不是商品資料，而是普通網頁文字！內容前 100 字為：\n{resp.text[:100]}")
            return

        missing = []
        for p in products:
            if not p.get("image_url") or p["image_url"] == "":
                missing.append({
                    "brand": p.get("brand"),
                    "name": p.get("name"),
                    "url": p.get("url"),
                })
        
        print(f"\n📊 【檢查結果】")
        print(f"總新品數：{len(products)}")
        print(f"缺少圖片：{len(missing)} 筆")
        for item in missing:
            print(f"  ❌ [{item['brand']}] {item['name']} → {item['url']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ 網頁連線錯誤 (HTTP Error)：代碼 {resp.status_code}")
        print("💡 解決策略：高機率是這個測試網址不對、停用了，或是需要開通登入權限喔！")
    except Exception as err:
        print(f"❌ 發生其他未預期錯誤: {err}")

check_missing_images()
