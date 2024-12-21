
from flask import Flask, request, send_file
import os
import random

app = Flask(__name__)

MAIN_IMAGES_PATH = "main_images"

@app.route('/search', methods=['GET'])
def search_image():
    keyword = request.args.get('keyword')
    if not keyword:
        return "Keyword parameter is missing", 400
    
    image_path = get_random_image(keyword)
    if image_path:
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return "No image found for the given keyword", 404

def get_random_image(object_class):
    # Retrieve a random image from the specified object class directory
    image_dir = os.path.join(MAIN_IMAGES_PATH, object_class)
    if not os.path.exists(image_dir):
        return None
    images = [img for img in os.listdir(image_dir) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
    return os.path.join(image_dir, random.choice(images)) if images else None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

