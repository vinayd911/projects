
import grpc
import os
import random
from concurrent import futures

import imagesearch_pb2
import imagesearch_pb2_grpc

MAIN_IMAGES_PATH = "main_images"

class ImageSearchService(imagesearch_pb2_grpc.ImageSearchServiceServicer):

    def SearchForKeyword(self, request, context):
        # Search for an image based on the keyword and return it
        keyword = request.keyword
        image_path = self._get_random_image(keyword)
        if image_path:
            with open(image_path, 'rb') as img_file:
                image_data = img_file.read()
            return imagesearch_pb2.ImageResponse(image_data=image_data)
        return imagesearch_pb2.ImageResponse(image_data=b'')

    def _get_random_image(self, object_class):
        # Retrieve a random image from the specified object class directory 
        image_dir = os.path.join(MAIN_IMAGES_PATH, object_class)
        if not os.path.exists(image_dir):
            return None
        images = [img for img in os.listdir(image_dir) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
        return os.path.join(image_dir, random.choice(images)) if images else None

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    imagesearch_pb2_grpc.add_ImageSearchServiceServicer_to_server(ImageSearchService(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

