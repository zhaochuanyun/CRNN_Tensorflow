import os

img_base_path = '/Users/mvpzhao/tools/python-workspace/mvpzhao-ai-examples/captcha/datasets/captcha_original_images'

text_list = []
for img_name in os.listdir(img_base_path):
    img_path = os.path.join(img_base_path, img_name)
    _, ret = os.path.splitext(img_path)
    if ret.lower() in ['.png', '.jpg']:
        text = img_path + ' ' + img_name[:4]
        text_list.append(text)

with open(os.path.join(img_base_path, 'text.txt'), 'w') as f:
    f.writelines([line + '\n' for line in text_list])
