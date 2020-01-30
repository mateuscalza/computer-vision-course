image = imread('../resources/bozo.jpg');
imshow(image);
line([1 900], [210 210], 'color', 'r');
figure;
plot(bozo_vermelho(210, :));