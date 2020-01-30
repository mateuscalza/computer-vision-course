CC=g++

CFLAGS := -std=c++11 hello_opencv.cpp
CFLAGS += `pkg-config --cflags --libs opencv4`

hello_opencv: hello_opencv.cpp
	$(CC) $(CFLAGS) -o hello_opencv.out
