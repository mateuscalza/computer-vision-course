n = 4;
x = linspace(-n, n);
y = x;

[U, V] = meshgrid(x, y);
sigma = 1;

z = (1/(2*pi*sigma^2)) .* exp(-(U .^ 2 + V .^ 2) / (sigma ^ 2));

colormap cool;
surf(U, V, z);
