image = imread('../resources/lena.jpg');
imshow(image);
image_blur = imgaussfilt(image, 4);
surf(double(rgb2gray(image_blur)), 'EdgeColor', 'none');
