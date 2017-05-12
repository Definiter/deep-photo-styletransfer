import os
from shutil import copyfile

result_prefix = 'result/result'
#result_suffix = ['_localaffine', '_localaffine_imagegradient', '_localaffine_imagegradient_rgb']
result_suffix = ['_relu1_2', '_relu2_2', '_relu3_2']
compare_path = 'result/compare'

if not os.path.exists(compare_path):
    os.makedirs(compare_path)

for i in range(60):
    flag = False
    for suffix in result_suffix:
        source = '{}{}/in{}.png_tar{}.png/affine_1000.png'.format(result_prefix, suffix, i + 1, i + 1)
        target = '{}/{}{}.png'.format(compare_path, i + 1, suffix)
        if os.path.exists(source):
            copyfile(source, target)
        else:
            flag = True
            break
    if flag:
         continue
    copyfile('data/content/in{}.png'.format(i + 1), '{}/{}_2content.png'.format(compare_path, i + 1))
    copyfile('data/style/tar{}.png'.format(i + 1), '{}/{}_1style.png'.format(compare_path, i + 1))