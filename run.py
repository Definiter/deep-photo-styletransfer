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
middle_result_path = 'data/middle_result/'

data = (#('day.jpg', 'snow.jpg'),
        #('snow.jpg', 'day.jpg'),
         ('in3.png', 'tar3.png'),
        #('in19.png', 'tar19.png'),
       )

matlab_run = False
for content_image, style_image in data:
    # Check if Laplacian exists
    if not (matlab_run or os.path.exists(laplacian_path + content_image + '.mat')):
        os.system('matlab -r \"run(\'gen_laplacian/gen_laplacian.m\')\"')
        matlab_run = True
    cmd = 'th deepmatting_seg.lua  -content_image ' + content_path + content_image + \
                                 ' -style_image ' + style_path + style_image + \
                                 ' -init_image random ' + \
                                 ' -content_seg ' + segmentation_path + content_image + \
                                 ' -style_seg ' + segmentation_path + style_image + \
                                 ' -laplacian ' + laplacian_path + content_image + '.mat' + \
                                 ' -result_path ' + result_path + content_image + '_' + style_image + \
                                 ' -num_iterations 1000 \
                                   -save_iter 50 \
                                   -print_iter 50 \
                                   -f_radius 15 \
                                   -f_edge 0.01'

    os.system(cmd)


                                 #' -init_image ' + middle_result_path + content_image + '_' + style_image + '.png' + \


