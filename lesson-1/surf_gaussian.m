image = imread('../resources/calza.jpg');
imshow(image);
image_blur = imgaussfilt(image, 4);
surf(double(rgb2gray(image_blur)), 'EdgeColor', 'interp');
colormap jet
