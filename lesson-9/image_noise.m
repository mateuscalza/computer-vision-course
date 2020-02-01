image = imread('../resources/pimentoes.jpg');
noise = uint8(abs(randn(size(image))));

sigma = 10;

image_with_noise = image + noise * sigma;
imshow(image_with_noise);

figure;
plot(image(200,:));
figure;
plot(image_with_noise(200,:));

