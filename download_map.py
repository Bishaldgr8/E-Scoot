
import requests
import os

def download_map():
    # IIIT Una coordinates: 31.481124, 76.190682
    # Yandex Static Maps API (ll=lon,lat)
    url = "https://static-maps.yandex.ru/1.x/?ll=76.190682,31.481124&size=650,450&z=16&l=map&pt=76.190682,31.481124,pm2rdm&lang=en_US"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        output_path = r"c:\Users\assdr\Desktop\New Project\assets\map_iiit_una.png"
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Map saved to {output_path}")
    else:
        print(f"Failed to download map. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    download_map()
