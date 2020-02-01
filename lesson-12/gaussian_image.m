img = imread('../resources/panda.jpg'); 
kernel_size = 31;

for sigma = 1:5:15
    h = fspecial('gaussian', kernel_size, sigma);
    output = imfilter(img, h);
    figure; imagesc(h);
    figure; imshow(output);
    pause; % PRESS ENTER
end
