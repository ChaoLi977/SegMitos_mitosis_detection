% Check if a patch contains positive pixels, if yes, it will be counted as positive patch.
% Since we will make more augmentation for positive patch, we need to get the list of all positive patches

gt_root='C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\gtImg1\4imgs_gt\';
dirname = {'01','02','03','04','05','06','07','08','09','10','11','12','13'}
%dirname = {'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16',...
%    '17','18','19','20','21','22','23'};
list_root = 'C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruth_ring_random\list';
fid_pos=fopen(fullfile(list_root, 'pos_all.txt'),'w');
fid_neg=fopen(fullfile(list_root, 'neg_all.txt'),'w');
for i=1:length(dirname)
    dir1=fullfile(gt_root, dirname{i});
    imglist=dir(fullfile(dir1, '\*.png'));
    for j=1:length(imglist)
        img=fullfile(dir1, imglist(j).name);
        im=imread(img);
        if max(max(im))<255
            fprintf(fid_neg, '%s\n', [dirname{i}, '/', imglist(j).name]);
        else
            fprintf(fid_pos, '%s\n', [dirname{i}, '/', imglist(j).name]);
        end
    end
end
fclose(fid_pos); fclose(fid_neg);
            
