import os

IMAGE_DIR = 'images'
INDEX_FILE = 'index.html'

def get_image_tags():
    image_files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]
    image_files.sort()
    tags = [f'<img src="{IMAGE_DIR}/{file}" alt="{file}" style="max-width: 200px;">' for file in image_files]
    return "\n".join(tags)

def update_index():
    image_html = get_image_tags()
    content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Image Gallery</title>
</head>
<body>
    <h1>Image Gallery</h1>
    {image_html}
</body>
</html>"""
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {INDEX_FILE} with {len(image_html.splitlines())} images.")

if __name__ == "__main__":
    update_index()
