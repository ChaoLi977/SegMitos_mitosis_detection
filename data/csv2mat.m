% convert the .csv format centroid label to .mat format, since we use the .mat format centroid when calculating the F-value of result 
% author:  Chao Li, 2017-06-16

gt_csv='C:\work\dataset\cell detection\TUPAC16\TUPAC2016\mitoses_ground_truth\';
cen_folder='C:\work\dataset\cell detection\TUPAC16\AMIDA13\GroundTruthMat\';  
dirname={'13/','14/','15/','16/','17/','18/','19/','20/','21/','22/','23/'}; % test set
for i=1:11
    if i<3
        img_dir='C:\work\dataset\cell detection\TUPAC16\TUPAC2016\mitoses_image_data_part_1';
    else
        img_dir='C:\work\dataset\cell detection\TUPAC16\TUPAC2016\mitoses_image_data_part_2';
    end
    FileList=dir(fullfile(img_dir,dirname{i},'*.tif'));
    folder=[gt_csv,dirname{i}];   
    for j=1:length(FileList)
        file=fullfile(folder,[FileList(j).name(1:end-3), 'csv']);
        if exist(file)==2
            M=csvread(file);
            centroid=M(:,1:2);
        else
            centroid=[];
        end
        name=fullfile(cen_folder,dirname{i}, [FileList(j).name(1:end-3), 'mat']  );
        if exist(fullfile(cen_folder, dirname{i}))~=7
            mkdir(fullfile(cen_folder, dirname{i}));
        end
        save(name, 'centroid');
    end
end







