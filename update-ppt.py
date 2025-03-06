import os
import glob
import shutil
import subprocess

ppt = glob.glob('./*.pptx')[0]
folder = 'ppt'
imagesDirectory = f'{folder}/ppt/media'
types = ('*.jpeg', '*.jpg')

os.system(f'7z x "{ppt}" -o{folder}')

images = []
for files in types:
    images.extend(glob.glob(f'{imagesDirectory}/{files}'))

for image in images:
	output = subprocess.check_output(f'exiftool -UserComment {image} -ext jpg -ext jpeg -q', shell=True).decode("utf-8")
	if(output != ''):
		newImage = output.split(': ')[1].split('\r\n')[0]
		print(newImage)
		shutil.copyfile(newImage, image)

os.system(f'cd {folder} && 7z u "../{ppt}" ./*')
shutil.rmtree(folder)
