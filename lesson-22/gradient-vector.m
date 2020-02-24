im = imread('../resources/calza.jpg');
img = rgb2gray(im);
[linhas, colunas] = size(img);
[dx, dy] = imgradient(img);    
[x, y] = meshgrid(1:colunas, 1:linhas);
imshow(img);
hold on;
quiver(x, y, dx, dy);
hold off;
