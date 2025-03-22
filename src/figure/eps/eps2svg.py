from PIL import Image
from pathlib import Path

current_path = Path("/root/Documents/vuepress-starter/src/figure/eps")
print(current_path)
for i in current_path.glob("*.eps"):
    print(i)
    eps_image = Image.open(i)
    eps_image.load(scale=10)
    eps_image.save(f"/root/Documents/vuepress-starter/src/figure/eps/{i.stem}.png")