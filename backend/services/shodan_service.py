# import shodan
# from config import SHODAN_API_KEY

# def search_assets(target):
#     try:
#         api = shodan.Shodan(SHODAN_API_KEY)
#         query = f'hostname:"{target}"'
#         results = api.search(query)

#         assets = []

#         for result in results['matches']:
#             assets.append({
#                 "ip": result.get("ip_str"),
#                 "port": result.get("port"),
#                 "org": result.get("org"),
#                 "country": result.get("location", {}).get("country_name"),
#                 "product": result.get("product")
#             })

#         return assets

#     except Exception as e:
#         print("Shodan Error:", e)
#         return []
import shodan
from config import SHODAN_API_KEY

def mock_assets():
    return [
        {"ip": "103.12.45.67", "port": 22},
        {"ip": "103.12.45.68", "port": 80},
        {"ip": "103.12.45.69", "port": 3389},
        {"ip": "103.12.45.70", "port": 443},
    ]

def search_assets(target):
    try:
        print("Loaded Shodan Key:", SHODAN_API_KEY)
        api = shodan.Shodan(SHODAN_API_KEY)
        
        query = f'hostname:"{target}"'
        results = api.search(query)

        assets = []

        for result in results['matches']:
            assets.append({
                "ip": result.get("ip_str"),
                "port": result.get("port")
            })

        if len(assets) == 0:
            return mock_assets()

        return assets

    except Exception as e:
        print("Shodan Error:", e)
        return mock_assets()