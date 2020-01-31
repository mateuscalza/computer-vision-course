bicicleta = imread('../resources/bicicleta.png');
golfinho = imread('../resources/golfinho.png');

imshow(bicicleta);
imshow(golfinho);

resultado = bicicleta * 0.6 + golfinho * 0.4;
imshow(resultado);
