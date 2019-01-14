% data augmentation for histopathology patch images
% for AMIDA 13
% author:  Chao Li, 2017-06-16

function []=augmentData()
saveDir='C:\work\dataset\cell detection\TUPAC16\AMIDA13\augImg\';
img_path='C:\work\dataset\cell detection\TUPAC16\AMIDA13\train\4imgs\';

fin=textread('C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\list\pos_all.txt','%s');
for i=1:length(fin)
    img=fin{i};
    pos_augment(img, img_path, saveDir);
    disp(img);
end

fin=textread('C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\list\neg_all.txt','%s');
for i=1:length(fin)
    img=fin{i};
    nega_augment(img,img_path, saveDir);
    disp(img);
end
end

function []=pos_augment(Img,img_path, saveDir)
% augment positive border patch
Imgfile=fullfile(img_path, [Img(1:end-4),'.bmp']);
I=imread(Imgfile);
IJ=jitterImage(I,'nPhi',9,'mPhi',180,'nTrn',3,'mTrn',20,'flip',1, 'hasChn',1);  %IJ is 9*9*2 images ,size:(521,521,162)
%montage2(uint8(IJ),{'hasChn',1})
name1=Img(1:end-4);
for i=[1:72,82:153]  % ´Ë´¦ÐèÒª¸Ä£¬gtImg1; gtImg2: +1
    if i<10
        imwrite(IJ(:,:,:,i), [saveDir,name1,'_0',num2str(i),'.jpg']);
    else
        imwrite(IJ(:,:,:,i), [saveDir,name1,'_',num2str(i),'.jpg']);
    end
end
end

function []=nega_augment(Img, img_path, saveDir)
Imgfile=fullfile(img_path, [Img(1:end-4),'.bmp']);
I=imread(Imgfile);
IJ=jitterImage(I, 'nPhi', 5, 'mPhi',180,'hasChn',1);
for i=1:4
    imwrite(IJ(:,:,:,i),  [saveDir,Img(1:end-4), '_0', num2str(i), '.jpg']);
end
end




