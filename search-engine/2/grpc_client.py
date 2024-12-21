
import grpc
import os

import imagesearch_pb2
import imagesearch_pb2_grpc

def get_image_from_server(keyword):
    #Request an image based on the keyword from the server and save it locally
    channel = grpc.insecure_channel('localhost:5000')
    stub = imagesearch_pb2_grpc.ImageSearchServiceStub(channel)
    
    # Create and send the request
    request = imagesearch_pb2.KeywordRequest(keyword=keyword)
    response = stub.SearchForKeyword(request)
    
    # Save the received image data
    output_dir = "received_images_grpc"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{keyword}.jpg")
    with open(output_path, 'wb') as img_file:
        img_file.write(response.image_data)
    print(f"Received image saved at: {output_path}")

if __name__ == '__main__':
    keyword = input("Enter the object class (keyword) to search for: ")
    get_image_from_server(keyword)

