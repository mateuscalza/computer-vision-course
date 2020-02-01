source = imread('../resources/albert-einstein.jpg');

kernel = [
    1 0 1;
    0 0 0;
    1 0 1
]; 
kernel_sum = sum(kernel, 'all');
normalized_kernel = kernel / kernel_sum;
disp(normalized_kernel);

output = source;

for i = 1:15
   output = imfilter(output, normalized_kernel, 'same', 'conv');
end

subplot(1, 2, 1); imshow(source); title('Original');
subplot(1, 2, 2); imshow(output); title('Result');
