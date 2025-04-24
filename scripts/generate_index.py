import os

IMAGE_DIR = 'public/images'
INDEX_FILE = 'public/index.html'

def get_image_tags():
    image_files = sorted(f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')))
    return '\n'.join([f'<img src="images/{f}" alt="{f}" style="max-width: 200px;">' for f in image_files])

def write_index():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Image Gallery</title>
</head>
<body>
    <h1>Image Gallery</h1>
    {get_image_tags()}
</body>
</html>
"""
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    write_index()
