img = imread('../resources/moon.jpg');  
imshow(img);

figure;
noisy_img = imnoise(img, 'salt & pepper', 0.03);
imshow(noisy_img);

figure;
median_filtered = medfilt2(noisy_img);
imshow(median_filtered);