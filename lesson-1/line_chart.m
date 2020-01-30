image = imread('../resources/bozo.jpg');
imshow(image);
line([1 900], [210 210], 'color', 'r');
figure;
red_image = image(:, :, 1);
plot(red_image(210, :));