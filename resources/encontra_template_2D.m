function [coordY coordX] = encontra_template_2D(template, imagem)
    c = normxcorr2(template, imagem);
    
    [matriz indice] = max(c(:));
    %[indiceY indiceX] = ind2sub(size(c), indice)
    [indiceY indiceX] = find(c==max(c(:)))

    coordY = indiceY-size(template, 1)+1;
    coordX = indiceX-size(template, 2)+1;
end