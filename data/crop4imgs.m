% crop the full histopathology images to 4*4 =16 patches
% author:  Chao Li, 2017-06-16

function []= crop4imgs()
dirname={'01','02','03','04','05','06','07','08','09','10','11','12', '13','14','15','16','17','18','19','20','21','22','23'};  % 01-12 for train, 13-23 for test

for n=1 :length(dirname)
    if str2num(dirname{n})<15
        folder_img='C:\work\dataset\cell detection\TUPAC16\TUPAC2016\mitoses_image_data_part_1';
    else
        folder_img='C:\work\dataset\cell detection\TUPAC16\TUPAC2016\mitoses_image_data_part_2';
    end
    folder=fullfile(folder_img, dirname{n});
    FileList=dir([folder,'\*.tif']);
    
    for i=1:length(FileList)        
        img4(folder_img,  dirname{n}, FileList(i).name);
    end
end

function []=img4(folder,dirname,  imgname)
img=fullfile(folder, dirname,  imgname);
I=imread(img);
H=500;   W=500;
Ic=uint8(zeros(H,W,3,16));
Ic(:,:,:,1)=I(1:H,1:W,:);
Ic(:,:,:,2)=I(1:H,W+1:2*W,:);
Ic(:,:,:,3)=I(1:H, 2*W+1:3*W, :);
Ic(:,:,:,4)=I(1:H, 3*W+1:4*W, :);

Ic(:,:,:,5)=I(H+1:2*H ,1:W, :);
Ic(:,:,:,6)=I(H+1:2*H ,W+1: 2*W, :);
Ic(:,:,:,7)=I(H+1:2*H , 2*W+1 : 3*W, :);
Ic(:,:,:,8)=I(H+1:2*H ,3*W+1 : 4*W, :);

Ic(:,:,:,9)=  I(2*H+1:3*H ,1:W, :);
Ic(:,:,:,10)=I(2*H+1:3*H ,W+1: 2*W, :);
Ic(:,:,:,11)=I(2*H+1:3*H , 2*W+1 : 3*W, :);
Ic(:,:,:,12)=I(2*H+1:3*H ,3*W+1 : 4*W, :);

Ic(:,:,:,13)=I(3*H+1:4*H ,1:W, :);
Ic(:,:,:,14)=I(3*H+1:4*H ,W+1: 2*W, :);
Ic(:,:,:,15)=I(3*H+1:4*H , 2*W+1 : 3*W, :);
Ic(:,:,:,16)=I(3*H+1:4*H ,3*W+1 : 4*W, :);

if str2num(dirname)<13
    save_root='C:\work\dataset\cell detection\TUPAC16\AMIDA13\train\4imgs\';
else
    save_root='C:\work\dataset\cell detection\TUPAC16\AMIDA13\test\4imgs\';
end

if exist(fullfile(save_root, dirname))~=7
    mkdir(fullfile(save_root, dirname));
end
for i=1:16
    if i<10
        file=fullfile(save_root, dirname, [imgname(1:end-4), '_0',num2str(i),'.bmp']);
    else
        file=fullfile(save_root, dirname, [imgname(1:end-4), '_', num2str(i),'.bmp']);
    end
    imwrite(Ic(:,:,:,i),file);
end
