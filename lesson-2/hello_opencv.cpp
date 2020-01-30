#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;

int main() {
    Mat image = imread("../resources/lena.png");
    if (image.empty()) {
        std::cerr << "Error loading image!" << std::endl;
        return -1;
    }
    imshow("Hello OpenCV!", image);
    waitKey(0);
    destroyAllWindows();
}
