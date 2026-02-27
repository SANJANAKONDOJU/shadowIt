import shodan

api = shodan.Shodan("Wa3dkeOJEv3a1ry5yOnvS56R37IvE63n")

try:
    info = api.info()
    print(info)
except Exception as e:
    print("Error:", e)