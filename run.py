import os
import math

# number of GPUs available
GPU_sum = 1
GPU_index = 0

content_path = 'data/content/'
style_path = 'data/style/'
segmentation_path = 'data/segmentation/'
laplacian_path = 'data/laplacian/'
result_path = 'result/result_temp/'
middle_result_path = 'data/middle_result/'

'''
data = [('in1.png', 'tar1.png'),
        ('in3.png', 'tar3.png'),
        ('in10.png', 'tar10.png'),
        ('in13.png', 'tar13.png'),
        ('in21.png', 'tar21.png'),
        ('in25.png', 'tar25.png'),
        ('in34.png', 'tar34.png'),
        ('in41.png', 'tar41.png')]
'''

data = []
for i in range(1):
    data.append(('in{}.png'.format(i + 1), 'tar{}.png'.format(i + 1)))

print data



if not os.path.exists(result_path):
    os.makedirs(result_path)
matlab_run = False
for content_image, style_image in data:
    # Check if Laplacian exists
    if not (matlab_run or os.path.exists(laplacian_path + content_image + '.mat')):
        os.system('matlab -r \"run(\'gen_laplacian/gen_laplacian.m\')\"')
        matlab_run = True
    options = [
        ['content_image', content_path + content_image],
        ['style_image', style_path + style_image],
        ###['style_image', middle_result_path + content_image + '_' + style_image + '.png'],
        ['init_image', middle_result_path + content_image + '_' + style_image + '.png'], # 'random'
        ###['init_image', content_path + content_image],
        ['content_seg', segmentation_path + content_image],
        ['style_seg', segmentation_path + style_image],
        ['result_path', result_path + content_image + '_' + style_image],
        # Interations
        ['num_iterations', 1000],
        ['save_iter', 50],
        ['print_iter', 50],
        # Local affine loss
        ['add_local_affine', 'true'],
        ['laplacian', laplacian_path + content_image + '.mat'],
        ['f_radius', 15],
        ['f_edge', 0.01],
        # Image Gradient loss
        ['add_image_gradient', 'true'],
        ['grad_weight', 1000],
        # Neural style loss
        #['content_layers', content_layer], # ADDED
    ]

    cmd = 'th deepmatting_seg.lua \\\n'
    for option in options:
        cmd += ' -{} {} \\\n'.format(option[0], option[1])
    print cmd
    os.system(cmd)

