img = imread('../resources/calza.jpg');
filtro = fspecial('sobel');
saida = imfilter(rgb2gray(img), filtro);
imshow(saida);
colormap gray
