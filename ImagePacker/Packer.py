

#from GUI import tk_entry_alb_suffix





def findtextures():
    import os, fnmatch
    import Settings
    #Set directory
    os.chdir(Settings.folder_path)

    #CREATE LIST WITH FOLDER FILES
    file_list = []
    for i in os.listdir():
        file_list.append(i) 


    def findfile(pattern, path):
        result = []
        for name in os.listdir():
            if fnmatch.fnmatch(name, pattern):
                result.append(name)
        return result
    #find('jpg', folder_path)
    Settings.tex_Albedo.append(findfile('*albedo*', Settings.folder_path))
    Settings.tex_Normal.append(findfile('*normal*', Settings.folder_path))
    Settings.tex_Roughness.append(findfile('*roughness*', Settings.folder_path))
    Settings.tex_Metalness.append(findfile('*metalness*', Settings.folder_path))
    Settings.tex_Height.append(findfile('*disp*', Settings.folder_path))
    Settings.tex_AO.append(findfile('*_ao*', Settings.folder_path))

if __name__ == "__main__":
    findtextures()

def ResetTextureValues():
    import Settings
    Settings.tex_Albedo = []
    Settings.tex_Normal = []
    Settings.tex_Roughness = []
    Settings.tex_Metalness = []
    Settings.tex_Height = []
    Settings.tex_AO = []

if __name__ == "__main__":
    ResetTextureValues()



def debug():
    import Settings
    print(Settings.tex_Albedo)
    print(Settings.tex_Normal)
    print(Settings.tex_Roughness)
    print(Settings.tex_Metalness)
    print(Settings.tex_AO)
    print(Settings.tex_Height)
if __name__ == "__main__":
    debug()


def convertimg():
    import os, fnmatch
    from shutil import copy2
    from PIL import Image as pillowimage
    import Settings

    import Settings
    print(Settings.tex_Albedo)
    print(Settings.tex_Normal)
    print(Settings.tex_Roughness)
    print(Settings.tex_Metalness)
    print(Settings.tex_AO)
    print(Settings.tex_Height)



    #print(dir(os))
    #print(os.getcwd())
    #Set directory
    os.chdir(Settings.folder_path)
    conv_fold_name = 'Converted'






    #CREATE FOLDER CONVERTED
    file_list = []
    for i in os.listdir():
        file_list.append(i) 
    if conv_fold_name not in file_list:
        os.mkdir('Converted')



    def imgprocess(srcname,folder,width,height,format, name, suffix):
        imgn = pillowimage.open(srcname)
        img_adj = imgn.resize((width, height))
        img_adj.save(folder+name+suffix+format)


    print('FINAL DEBUG BEFOR CONVERSION')
    debug()

        
    if Settings.tex_Albedo:
        if not Settings.tex_Albedo == 'None':
            print('Converting: '+Settings.tex_albedo)
            imgprocess(Settings.tex_Albedo,Settings.destination_folder, int(Settings.width_px), int(Settings.height_px),Settings.c_format, Settings.c_TextureName,Settings.c_AlbedoSuffix)
   
    if Settings.tex_Normal:
        if not Settings.tex_Normal == 'None':
            print('Converting: '+Settings.tex_normal)
            imgprocess(Settings.tex_Normal,Settings.destination_folder, int(Settings.width_px), int(Settings.height_px),Settings.c_format, Settings.c_TextureName,Settings.c_NormalSuffix)
    
    if Settings.tex_Roughness:
        if not Settings.tex_Roughness == 'None':
            print('Converting: '+Settings.tex_roughness)
            imgprocess(Settings.tex_Roughness,Settings.destination_folder, int(Settings.width_px), int(Settings.height_px),Settings.c_format, Settings.c_TextureName,Settings.c_RoughnessSuffix)
    
    if Settings.tex_Metalness:
        if not Settings.tex_Metalness == 'None':
            print('Converting: '+Settings.tex_metalness)
            imgprocess(Settings.tex_Metalness,Settings.destination_folder, int(Settings.width_px), int(Settings.height_px),Settings.c_format, Settings.c_TextureName,Settings.c_MetalnessSuffix)
    
    if Settings.tex_Height:
        if not Settings.tex_Height == 'None':
            print('Converting: '+Settings.tex_height)
            imgprocess(Settings.tex_Height,Settings.destination_folder, int(Settings.width_px), int(Settings.height_px),Settings.c_format, Settings.c_TextureName,Settings.c_HeightSuffix)
    if Settings.tex_AO:
        if not Settings.tex_AO == 'None':
            print('Converting: '+Settings.tex_AO)
            imgprocess(Settings.tex_AO,Settings.destination_folder, int(Settings.width_px), int(Settings.height_px),Settings.c_format, Settings.c_TextureName,Settings.c_AOSuffix)
    
    print('DONE')

if __name__ == "__main__":
    convertimg()






















#IF RESOLUTION LEFT AT NONE FUNCTION KEEPS THE ORIGINAL RESOLUTION

#EXAMPLE:
#dir = r'C:\Users\lreznicek\Desktop\Asphalt_Fine_tk3mebkew_8K_surface_ms\packer'
#aimgName = 'TESTIMAGE.tga'
#aimgR = 'tk3mebkew_8K_AO.jpg'
#aimgG = 'tk3mebkew_8K_Roughness.jpg'
#aimgB = None
#packRGBA(dir,aimgName,SimgR=None, SimgG=aimgG,SimgB=aimgB,imgResW=None,imgResH=None, SimgA=aimgR)

def packRGBA(dir,imgName, SimgR=None, SimgG=None, SimgB=None, SimgA=None, imgResW=None, imgResH=None):
    import os
    from PIL import Image as P_Image
    from PIL import ImageOps as P_ImageOps

    #SET DIRECTORY
    os.chdir(dir)

    #DETERMINE SOURCE RESOLUTION            
    for i in [SimgR,SimgG,SimgB,SimgA]:
        if i == None:
            continue
        else:
            imr = P_Image.open(i)
            SwidthR, SheightR = imr.size
            break

    #SET SOURCE WIDTH AND HEIGHT IF NOT SPECIFIED IN FUNCTION
    if imgResW is None:
        imgResW = SwidthR

    if imgResH is None:
        imgResH = SheightR

    tRes = (imgResW, imgResH)

    #CREATE EMPTY IMAGES IF NONE ARE SPECIFIED IN FUNCTION, CONVERT INPUT TEXTURES TO GRAYSCALE, SET RESOLUTION
    if SimgR is None:
        imgRg = P_Image.new('L', tRes, color='#808080')
    else:
        imgR = P_Image.open(SimgR)
        imgR = imgR.resize(tRes)
        imgRg = P_ImageOps.grayscale(imgR)

    if SimgG is None:
        imgGg = P_Image.new('L',tRes,color='#808080')
    else:
        imgG = P_Image.open(SimgG)
        imgG = imgG.resize(tRes)
        imgGg = P_ImageOps.grayscale(imgG)
    
    if SimgB is None:
        imgBg = P_Image.new('L',tRes,color='#808080')
    else:
        imgB = P_Image.open(SimgB)
        imgB = imgB.resize(tRes)
        imgBg = P_ImageOps.grayscale(imgB)

    if SimgA is None:
        pass
    else:
        imgA = P_Image.open(SimgA)
        imgA = imgA.resize(tRes)
        imgAg = P_ImageOps.grayscale(imgA)        

    
    #MERGE GRAYSCALE IMAGES    
    if SimgA is None:
        imageRGB = P_Image.merge('RGB', (imgRg,imgGg,imgBg))
    else:
        imageRGB = P_Image.merge('RGBA', (imgRg,imgGg,imgBg,imgAg))
    
    #SAVE PACKED IMAGE  
    imageRGB.save(imgName)

    #OUTPUT
    print('PACKED')

if __name__ == "__main__":
    pass












