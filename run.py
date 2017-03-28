import os
import math

# number of GPUs available
GPU_sum = 1
GPU_index = 0

content_path = 'data/content/'
style_path = 'data/style/'
segmentation_path = 'data/segmentation/'
laplacian_path = 'data/laplacian/'
result_path = 'data/result/'

data = (#('day.jpg', 'snow.jpg'),
        #('snow.jpg', 'day.jpg')
         ('in1.png', 'tar15.png)
       )

matlab_run = False
for content_image, style_image in data:
    # Check if Laplacian exists
    if not (matlab_run or os.path.exists(laplacian_path + content_image + '.mat')):
        os.system('matlab -r \"run(\'gen_laplacian/gen_laplacian.m\')\"')
        matlab_run = True
    cmd = 'th deepmatting_seg.lua  -content_image ' + content_path + content_image + \
                                 ' -style_image ' + style_path + style_image + \
                                 ' -init_image ' + content_path + content_image + \
                                 ' -content_seg ' + segmentation_path + content_image + \
                                 ' -style_seg ' + segmentation_path + style_image + \
                                 ' -laplacian ' + laplacian_path + content_image + '.mat' + \
                                 ' -result_path ' + result_path + content_image + '_' + style_image + \
                                 ' -num_iterations 1000 \
                                   -save_iter 100 \
                                   -print_iter 100 \
                                   -f_radius 15 \
                                   -f_edge 0.01'
    
    os.system(cmd)




