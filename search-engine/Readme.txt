Readme File for Team 22's project:
Folder 1 is for question 3, just containerized
Folder 2 is for question 4, containerized grpc
The random image is being saved to the same file with the name of the keyword in client_output folder, refresh and open image to get the latest output

Question 3:
Server side:
docker build -t image-search-server -f Dockerfile_server .
docker run -it --network="host" image-search-server
Client side:
docker build -t image-search-client -f Dockerfile_client . 
docker run -it --network="host" -v $(pwd)/client_output:/app/received_images image-search-client
Enter the object class (keyword) to search for: car

grpc setup:
pip install grpcio grpcio-tools
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. imagesearch.proto

Question 4:
Server side:
docker build -t grpc-image-search-server -f Dockerfile_server .
docker run --network="host" grpc-image-search-server
Client side:
docker build -t grpc-image-search-client -f Dockerfile_client .
docker run --network="host" -v $(pwd)/client_output:/app/received_images_grpc -it grpc-image-search-client

Current issues:
Executing the above "docker run ..." commands is not possible in a directory that has capital letters, please verify with pwd before execution 