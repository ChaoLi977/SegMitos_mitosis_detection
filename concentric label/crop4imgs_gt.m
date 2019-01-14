
% crop the full label images to 4*4 =16 patches
% for AMIDA 13
% author:  Li Chao, 2017-06-16

function []= crop4imgs_gt()
folder_g='C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\gtImg1\';
% run this m file multiple times, change the folder name for gtImg1-gtImg4. 
dirname={'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16',...
    '17','18','19','20','21','22','23'}; 
for n=1:length(dirname)
    folder=[folder_g,dirname{n},'\'];
    FileList=dir([folder,'*.png']);
    
    for i=1:length(FileList)
        img4([folder,  FileList(i).name]);
    end
end

function []=img4(img)
I=imread(img);
I=imresize(I, [2000,2000]);
H=500;   W=500;
Ic=uint8(zeros(H,W,16));
Ic(:,:,1)=I(1:H,1:W);
Ic(:,:,2)=I(1:H,W+1:2*W);%figure;imshow(I2);
Ic(:,:,3)=I(1:H, 2*W+1:3*W);%figure;imshow(I3);
Ic(:,:,4)=I(1:H, 3*W+1:4*W);%figure;imshow(I4);

Ic(:,:,5)=I(H+1:2*H ,1:W);
Ic(:,:,6)=I(H+1:2*H ,W+1: 2*W);
Ic(:,:,7)=I(H+1:2*H , 2*W+1 : 3*W);
Ic(:,:,8)=I(H+1:2*H ,3*W+1 : 4*W);

Ic(:,:,9)=  I(2*H+1:3*H ,1:W);
Ic(:,:,10)=I(2*H+1:3*H ,W+1: 2*W);
Ic(:,:,11)=I(2*H+1:3*H , 2*W+1 : 3*W);
Ic(:,:,12)=I(2*H+1:3*H ,3*W+1 : 4*W);

Ic(:,:,13)=I(3*H+1:4*H ,1:W);
Ic(:,:,14)=I(3*H+1:4*H ,W+1: 2*W);
Ic(:,:,15)=I(3*H+1:4*H , 2*W+1 : 3*W);
Ic(:,:,16)=I(3*H+1:4*H ,3*W+1 : 4*W);

folder_g='C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\gtImg1\';
savefile = fullfile(folder_g, '4imgs_gt');
folder=fullfile(savefile, img(end-8:end-6));
if exist(folder)~=7
    mkdir(folder);
end
name=img(end-8:end-4);
for i=1:16
    if i<10
        file=fullfile(savefile, [name, '_0',num2str(i),'.png']);
    else
        file=fullfile(savefile, [name, '_',num2str(i),'.png']);
    end
    imwrite(Ic(:,:,i),file);
end
