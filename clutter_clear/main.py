import os
def createIfNotExist(folder):
     if not  os.path.exists(folder):
         os.makedirs(folder)

def move(folder,files):
      for file in files:
          os.replace(file,f"{folder}/{file}")
if __name__ == "__main__":
    createIfNotExist("Medias")
    createIfNotExist("Documents")
    createIfNotExist("Images")
    createIfNotExist("Zip files")
    createIfNotExist("Applications")
    createIfNotExist("Others")
    files = os.listdir()  
    files.remove("main.py")
    documentsext=[".docx", ".doc", ".pdf", '.csv',".pptx", ".txt"]
    imagesext= [".jpg",".jpeg",'.png']
    zipext= ['.zip',".rar"]
    mediaext=['.mp3','.mp4','.mkv']
    applications = [".exe",".apk",".msi"]
    othersext = zipext+imagesext+documentsext+mediaext+applications

    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaext]
    documents = [file for file in files if os.path.splitext(file)[1].lower() in documentsext]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imagesext]
    zips = [file for file in files if os.path.splitext(file)[1].lower() in zipext]
    application =  [file for file in files if os.path.splitext(file)[1].lower() in applications]
    # others = [file for file in files if os.path.splitext(file)[1].lower() not in othersext]  
    others= []
    folders=[]
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaext) and (ext not in documentsext) and (ext not in imagesext) and (ext not in applications) and os.path.isfile(file):
          others.append(file)
    move("Images", images)
    move("Zip files", zips)
    move("Documents", documents)
    move("Medias", medias)
    move("Applications", application)
    move("Others", others)
    
