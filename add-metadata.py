import os
import glob

images = glob.glob('images/*')
for image in images:
    os.system(f'exiftool "{image}" -charset iptc=utf8 -L -UserComment="{image}" -overwrite_original -q -m')
