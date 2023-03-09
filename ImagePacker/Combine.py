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



