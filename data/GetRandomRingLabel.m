%  convert the single-pixel centroid label to concentric label, and the radii of two circles are random
% author: Chao Li
% date:2017/6/16
% for AMIDA 13 dataset
gt_Img='$AMIDA13\GroundTruth_ring_random\gtImg1\';  % the dir to save the concentric labels
% Noted that in our experiments we run this m file multiple times, 
% so that we can get multiple random concentric label images (e.g., gtImg1, gtImg2, gtImg3, gtImg4)

dirname = {'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16',...
    '17','18','19','20','21','22','23'};
for i=1:length(dirname)
    % if you download the AMIDA13 from TUPAC16 website, the data are in different folders
    if str2num(dirname{i})<=14
        rt_folder = '$AMIDA13\mitoses_image_data_part_1\';
    else
        rt_folder = '$AMIDA13\mitoses_image_data_part_2\';
    end
    gt_csv='$AMIDA13\mitoses_ground_truth';  % ground truth dir
    folder=fullfile(gt_csv, dirname{i});
    FileList=dir(fullfile(rt_folder, dirname{i}, '\*.tif'));
    save_gtImg=[gt_Img,dirname{i},'\'];
    if exist(save_gtImg)~=7
        mkdir(save_gtImg);
    end
    for j=1:length(FileList) 
        img=uint8(zeros(2000,2000));
        file=fullfile(folder,[FileList(j).name(1:end-3), 'csv']);   
        if exist(file)==2
            M=csvread(file);
            centroid=M(:,1:2);
            for m=1:size(centroid,1)
                r=randi([10,17]);  % random a small r                     
                alpha=1.5+rand;  %random the ratio, 1.5-2.5
                R=round(alpha*r);               
                xc=centroid(m,1);   yc=centroid(m,2);
                fprintf('r:%d R:%d\n', r,R);
                
                for x=xc-R:xc+R
                    for y=yc-R:yc+R
                        if (x-xc)^2+(y-yc)^2<=r^2
                            x1=max(min(2000, x),1);  y1=max(min(2000, y),1);
                            img(x1, y1)=255;  % we use this value and transfer it to 1 in data layer 
                        elseif (x-xc)^2+(y-yc)^2<=R^2
                            x1=max(min(2000, x),1);  y1=max(min(2000, y),1);
                            img(x1, y1)=120;   % we use this value and transfer it to 255 in
                        end
                    end
                end
            end
        else
            centroid = [];
        end
        saveImg=[save_gtImg,FileList(j).name(1:end-4),'.png'];
        imwrite(img,saveImg) ;
    end
end





