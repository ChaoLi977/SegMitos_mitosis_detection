% data augmentation for label images of random concentric
% For four different random concentric labels (gtImg1-gtImg4), we only take part of augmented images. 

% for AMIDA 13
% author:  Chao Li, 2017-06-16

function []=augmentData_gt()
saveDir='C:\work\dataset\cell detection\TUPAC16\AMIDA13\augImg_gt_ring_random\';
gt_path='C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\gtImg4\4imgs_gt\';

fin=textread('C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\list\pos_all.txt','%s');
for i=1:length(fin)
    img=fin{i};
    path1 = 'C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\';
    path2 = '\4imgs_gt\'
    for gtInd=1:4
        gt_path = sprintf('%sgtImg%d%s', path1,gtInd,path2)        
        pos_augment(img, gt_path, saveDir, gtInd);
    end
    disp(img);
end
 
fin=textread('C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\list\neg_all.txt','%s');
for i=1:length(fin)
    img=fin{i};
    nega_augment(img,gt_path, saveDir);
    disp(img);
end
end

function []=pos_augment(Img,gt_path, saveDir, gtInd)
% augment positive patch
Imgfile=fullfile(gt_path, Img);
I=imread(Imgfile);
IJ=jitterImage(I,'nPhi',9,'mPhi',180,'nTrn',3,'mTrn',20,'flip',1);  %IJ is 9*9*2 images
%montage2(uint8(IJ),{'hasChn',1})
name1=Img(1:end-4);
for i=[1:4:72,82:4:153]+gtInd-1  
    if i<10
        imwrite(IJ(:,:,i), [saveDir,name1,'_0',num2str(i),'.png']);
    else
        imwrite(IJ(:,:,i), [saveDir,name1,'_',num2str(i),'.png']);
    end
end
end

function []=nega_augment(Img, gt_path, saveDir)
Imgfile=fullfile(gt_path, Img);
I=imread(Imgfile);
IJ=jitterImage(I, 'nPhi', 5, 'mPhi',180);
for i=1:4
    imwrite(IJ(:,:,i),  [saveDir,Img(1:end-4), '_0', num2str(i), '.png']);
end
end




