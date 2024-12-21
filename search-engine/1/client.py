
import requests
import os

# Constants
HOST = '127.0.0.1'
PORT = 5000
SAVE_DIR = "received_images"
URL = f"http://{HOST}:{PORT}/search"

def get_image_from_server(keyword):
    """Connect to the server via HTTP and retrieve the image."""
    
    # Check if save directory exists
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    
    # Send an HTTP GET request to the server with the keyword as a parameter
    response = requests.get(URL, params={"keyword": keyword})
    
    # Check if the response contains an image
    if response.status_code == 200 and response.headers["content-type"].startswith("image"):
        image_path = os.path.join(SAVE_DIR, f"{keyword}.jpg")
        with open(image_path, 'wb') as img_file:
            img_file.write(response.content)
        print(f"Received image saved at: {image_path}")
    else:
        print(f"Failed to retrieve image. Server responded with status code: {response.status_code}")


keyword = input("Enter the object class (keyword) to search for: ")
get_image_from_server(keyword)

