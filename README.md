# PowerPoint Image Auto-Updater | Actualizador Automático de Imágenes en PowerPoint  

## 🇺🇸 English  

This script automates the replacement of images in a PowerPoint file. It updates images from the **images** folder while preserving their positions and sizes in the presentation.  

### Requirements  
- **Python 3** → [Download here](https://www.python.org/)  
- **ExifTool** → [Download here](https://exiftool.org/)  
- **7-Zip** → [Download here](https://www.7-zip.org/)  

### Usage  
#### First Configuration  
1. Place all images inside the **images** folder.  
2. Run `add-metadata.py` to add the image name as a metadata comment.  
3. Insert the images from the **images** folder into the PowerPoint file (the PowerPoint file must be located in the project folder).  
4. Save the PowerPoint file.  

#### Updating the Images  
1. Replace the images in the **images** folder, ensuring the file names remain unchanged.  
2. Run `add-metadata.py` to update metadata.  
3. Run `update-ppt.py` to replace the images inside the PowerPoint file.  

### Important  
- This script relies on image names for replacement. If an image named **"image1.jpg"** exists in the PowerPoint file, it will be replaced by the new **"image1.jpg"** from the **images** folder.  
- Ensure all image names remain consistent to avoid mismatches.  

---

## 🇪🇸 Español  

Este script automatiza la sustitución de imágenes en un archivo de PowerPoint. Actualiza las imágenes desde la carpeta **images**, manteniendo su posición y tamaño en la presentación.  

### Requisitos  
- **Python 3** → [Descargar aquí](https://www.python.org/)  
- **ExifTool** → [Descargar aquí](https://exiftool.org/)  
- **7-Zip** → [Descargar aquí](https://www.7-zip.org/)  

### Uso  
#### Primera configuración  
1. Coloca todas las imágenes dentro de la carpeta **images**.  
2. Ejecuta `add-metadata.py` para agregar el nombre de la imagen como comentario de metadatos.  
3. Agrega las imágenes desde la carpeta **images** al archivo de PowerPoint (el archivo debe estar en la carpeta del proyecto).  
4. Guarda el archivo de PowerPoint.  

#### Actualización de las imágenes  
1. Reemplaza las imágenes en la carpeta **images**, asegurándote de que los nombres de archivo sean los mismos.  
2. Ejecuta `add-metadata.py` para actualizar los metadatos.  
3. Ejecuta `update-ppt.py` para reemplazar las imágenes en el archivo de PowerPoint.  

### Importante  
- Este script se basa en los nombres de archivo para reemplazar imágenes. Si una imagen en PowerPoint se llama **"image1.jpg"**, será reemplazada por la nueva **"image1.jpg"** de la carpeta **images**.  
- Asegúrate de mantener los nombres de archivo consistentes para evitar errores.  
