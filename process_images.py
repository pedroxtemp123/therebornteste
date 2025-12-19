import requests
from PIL import Image
import io
import os

os.makedirs("client/public/assets/weapons", exist_ok=True)

urls = {
    "vortex_gatlin_pistol.png": "https://i.ibb.co/mVCJTJWh/Gemini-Generated-Image-yw25mtyw25mtyw25.png",
    "chaos_ray_zapper.png": "https://i.ibb.co/MxG0xZ9G/Gemini-Generated-Image-w2oyow2oyow2oyow.png"
}

def remove_black_background(img):
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = []
    for item in datas:
        # Check if pixel is close to black
        # (0, 0, 0) is black. Let's be a bit lenient, e.g. < 30
        if item[0] < 30 and item[1] < 30 and item[2] < 30:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img

for filename, url in urls.items():
    print(f"Downloading {filename}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(io.BytesIO(response.content))
        
        print(f"Processing {filename}...")
        img = remove_black_background(img)
        
        save_path = f"client/public/assets/weapons/{filename}"
        img.save(save_path, "PNG")
        print(f"Saved to {save_path}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
