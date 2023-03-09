
import Packer
import tkinter as tk
#TKINTER
root = tk.Tk()
root.title("Convert Images")
root.geometry('420x400')
import Settings
import Packer 





#SOURCE FOLDER - LABEL 
tk_label_source = tk.Label(root, text='Source folder: ')
tk_label_source.grid(sticky="e",row=0, column=0)
#SOURCE FOLDER - ENTRY 
mystringSource = tk.StringVar(root)
tk_entry_source = tk.Entry(root,textvariable = mystringSource, width = 20)
tk_entry_source.grid(sticky="w",row=0, column=1, columnspan = 2, pady=10)

#TEXTURE NAME - LABEL 
tk_label_albedo_name = tk.Label(root, text='Texture name: ')
tk_label_albedo_name.grid(sticky="e",row=1, column=0, pady=10)
#TEXTURE NAME - ENTRY
mystringTextureName = tk.StringVar(root)
tk_entry_alb_name = tk.Entry(root, textvariable = mystringTextureName)
tk_entry_alb_name.grid(sticky="w", row=1, column=1)
tk_entry_alb_name.insert(tk.END, 'Texture name')

#RESOLUTION_X - LABEL 
tk_label_resolution_x_name = tk.Label(root, text='Resolution: ')
tk_label_resolution_x_name.grid(sticky="e",row=2, column=0, pady=10)
#RESOLUTION_X - ENTRY
mystring_resolution_x = tk.StringVar(root)
tk_entry_resolution_x_name = tk.Entry(root, textvariable = mystring_resolution_x,width = 5)
tk_entry_resolution_x_name.grid(sticky="w", row=2, column=1, pady=10)
tk_entry_resolution_x_name.insert(tk.END, 2048)

#RESOLUTION - LABEL 
tk_label_resolution_x_name = tk.Label(root, text='x')
tk_label_resolution_x_name.grid(sticky="w",row=2, column=1,padx=(39, 0), pady=10)
#RESOLUTION_Y - ENTRY
mystring_resolution_y = tk.StringVar(root)
tk_entry_resolution_y_name = tk.Entry(root, textvariable = mystring_resolution_y,width = 5)
tk_entry_resolution_y_name.grid(sticky="w", row=2, column=1,padx=(56, 0), pady=10)
tk_entry_resolution_y_name.insert(tk.END, 2048)

#RESOLUTION - LABEL 
tk_label_resolution_px_name = tk.Label(root, text='px')
tk_label_resolution_px_name.grid(sticky="w",row=2, column=1,padx=(90, 0), pady=10)




#ALBEDO - ENTRY 

myStringAlbedo = tk.StringVar(root)
tk_entry_Albedo = tk.Entry(root, textvariable = myStringAlbedo,width = 30)
tk_entry_Albedo.grid(sticky="w",row=4, column=1,pady=2)
if Settings.tex_Albedo:
    tk_entry_Albedo.insert(tk.END, Settings.tex_Albedo[0])
else:
    tk_entry_Albedo.insert(tk.END, 'None')

#ALBEDO SUFFIX - LABEL 
tk_label_albedo_suffix = tk.Label(root, text='Albedo: ')
tk_label_albedo_suffix.grid(sticky="e",row=4, column=0)
#ALBEDO SUFFIX - ENTRY 
mystringAlbedoSuffix = tk.StringVar(root)
tk_entry_alb_suffix = tk.Entry(root, textvariable = mystringAlbedoSuffix,width = 10)
tk_entry_alb_suffix.grid(sticky="w",row=4, column=2,pady=2)
tk_entry_alb_suffix.insert(tk.END, Settings.c_AlbedoSuffix)


#NORMAL - ENTRY 

mystringNormal = tk.StringVar(root)
tk_entry_Normal = tk.Entry(root, textvariable = mystringNormal,width = 30)
tk_entry_Normal.grid(sticky="w",row=5, column=1,pady=2)
if Settings.tex_Normal:
    tk_entry_Normal.insert(tk.END, Settings.tex_Normal[0])
else:
    tk_entry_Normal.insert(tk.END, 'None')
#NORMAL SUFFIX - LABEL 
tk_label_normal_suffix = tk.Label(root, text='Normal: ')
tk_label_normal_suffix.grid(sticky="e",row=5, column=0)
#NORMAL SUFFIX - ENTRY 
mystringNormalSuffix = tk.StringVar(root)
tk_entry_norm_suffix = tk.Entry(root, textvariable = mystringNormalSuffix,width = 10)
tk_entry_norm_suffix.grid(sticky="w",row=5, column=2,pady=2)
tk_entry_norm_suffix.insert(tk.END, Settings.c_NormalSuffix)


#ROUGHNESS - ENTRY 

mystringRoughness = tk.StringVar(root)
tk_entry_Roughness = tk.Entry(root, textvariable = mystringRoughness,width = 30)
tk_entry_Roughness.grid(sticky="w",row=6, column=1,pady=2)
if Settings.tex_Roughness:
    tk_entry_Roughness.insert(tk.END, Settings.tex_Roughness[0])
else:
    tk_entry_Roughness.insert(tk.END, 'None')

#ROUGHNESS SUFFIX - LABEL 
tk_label_roughness_suffix = tk.Label(root, text='Roughness: ')
tk_label_roughness_suffix.grid(sticky="e",row=6, column=0)
#ROUGHNESS SUFFIX - ENTRY 
mystringRoughnessSuffix = tk.StringVar(root)
tk_entry_Roughness_suffix = tk.Entry(root, textvariable = mystringRoughnessSuffix,width = 10)
tk_entry_Roughness_suffix.grid(sticky="w",row=6, column=2,pady=2)
tk_entry_Roughness_suffix.insert(tk.END, Settings.c_RoughnessSuffix)


#METALNESS - ENTRY 

mystringMetalness = tk.StringVar(root)
tk_entry_Metalness = tk.Entry(root, textvariable = mystringMetalness,width = 30)
tk_entry_Metalness.grid(sticky="w",row=7, column=1,pady=2)
if Settings.tex_Metalness:
    tk_entry_Metalness.insert(tk.END, Settings.tex_Metalness[0])
else:
    tk_entry_Metalness.insert(tk.END, 'None')
#METALNESS SUFFIX - LABEL 
tk_label_Metalness_suffix = tk.Label(root, text='Metalness: ')
tk_label_Metalness_suffix.grid(sticky="e",row=7, column=0)
#METALNESS SUFFIX - ENTRY 
mystringMetalnessSuffix = tk.StringVar(root)
tk_entry_Metalness_suffix = tk.Entry(root, textvariable = mystringMetalnessSuffix,width = 10)
tk_entry_Metalness_suffix.grid(sticky="w",row=7, column=2,pady=2)
tk_entry_Metalness_suffix.insert(tk.END, Settings.c_MetalnessSuffix)



#HEIGHT - ENTRY 

mystringHeight = tk.StringVar(root)
tk_entry_Height = tk.Entry(root, textvariable = mystringHeight,width = 30)
tk_entry_Height.grid(sticky="w",row=8, column=1,pady=2)
if Settings.tex_Height:
    tk_entry_Height.insert(tk.END, Settings.tex_Height[0])
else:
    tk_entry_Height.insert(tk.END, 'None')
#HEIGHT SUFFIX - LABEL 
tk_label_height_suffix = tk.Label(root, text='Height: ')
tk_label_height_suffix.grid(sticky="e",row=8, column=0)
#HEIGHT SUFFIX - ENTRY 
mystringHeightSuffix = tk.StringVar(root)
tk_entry_Height_suffix = tk.Entry(root, textvariable = mystringHeightSuffix,width = 10)
tk_entry_Height_suffix.grid(sticky="w",row=8, column=2,pady=2)
tk_entry_Height_suffix.insert(tk.END, Settings.c_HeightSuffix)


#AO - ENTRY 

mystringAO = tk.StringVar(root)
tk_entry_AO = tk.Entry(root, textvariable = mystringAO,width = 30)
tk_entry_AO.grid(sticky="w",row=9, column=1,pady=2)
if Settings.tex_AO:
    tk_entry_AO.insert(tk.END, Settings.tex_AO[0])
else:
    tk_entry_AO.insert(tk.END, 'None')
#AO SUFFIX - LABEL 
tk_label_AO_suffix = tk.Label(root, text='AO: ')
tk_label_AO_suffix.grid(sticky="e",row=9, column=0)
#AO SUFFIX - ENTRY 
mystringAOSuffix = tk.StringVar(root)
tk_entry_AO_suffix = tk.Entry(root, textvariable = mystringAOSuffix,width = 10)
tk_entry_AO_suffix.grid(sticky="w",row=9, column=2,pady=2)
tk_entry_AO_suffix.insert(tk.END, Settings.c_AOSuffix)



#SET VARIABLES IN SETTINGS
Packer.ResetTextureValues()
def myString_Source():
    Settings.folder_path = mystringSource.get()

def myString_TextureName():
    Settings.c_TextureName = mystringTextureName.get()

def myString_Resolution_X_Name():
    Settings.width_px = mystring_resolution_x.get()

def myString_Resolution_Y_Name():
    Settings.height_px = mystring_resolution_y.get()

def myString_AlbedoSuffix():
    print('Inside albedo suffix is this shit: ')
    print(mystringAlbedoSuffix.get())
    Settings.c_AlbedoSuffix = mystringAlbedoSuffix.get()

def myString_NormalSuffix():
    Settings.c_NormalSuffix = mystringNormalSuffix.get()

def myString_RoughnessSuffix():
    Settings.c_RoughnessSuffix = mystringRoughnessSuffix.get()

def myString_MetalnessSuffix():
    Settings.c_MetalnessSuffix = mystringMetalnessSuffix.get()

def myString_HeightSuffix():
    Settings.c_HeightSuffix = mystringHeightSuffix.get()

def myString_AOSuffix():
    Settings.c_AOSuffix = mystringAOSuffix.get()


#SET SETTINGS EXEBUTTON
def myString_Albedo():
    Settings.tex_Albedo = myStringAlbedo.get()

def myString_Normal():
    Settings.tex_Normal = mystringNormal.get()

def myString_Roughness():
    Settings.tex_Roughness = mystringRoughness.get()

def myString_Metalness():
    Settings.tex_Metalness = mystringMetalness.get()

def myString_AO():
    Settings.tex_AO = mystringAO.get()

def myString_Height():
    Settings.tex_Height[0] = mystringHeight.get()




#ADDVALUES FROM SETTINGS INTO GUI
def myString_Find():
    Packer.ResetTextureValues()
    Packer.findtextures()


    if Settings.tex_Albedo[0]:
        myStringAlbedo.set(Settings.tex_Albedo[0][0])
    else:
        myStringAlbedo.set('None')

    if Settings.tex_Normal[0]:
        mystringNormal.set(Settings.tex_Normal[0][0])
    else:
        mystringNormal.set('None')

    if Settings.tex_Roughness[0]:
        mystringRoughness.set(Settings.tex_Roughness[0][0])
    else:
        mystringRoughness.set('None')

    if  Settings.tex_Metalness[0]:
        mystringMetalness.set(Settings.tex_Metalness[0][0])
    else:
        mystringMetalness.set('None') 

    if Settings.tex_AO[0]:
        mystringAO.set(Settings.tex_AO[0][0])
    else:

        mystringAO.set('None')

    if Settings.tex_Height[0]:
        mystringHeight.set(Settings.tex_Height[0][0])
    else:
        mystringHeight.set('None')
    print('DEBUG FIND TEXTURES.........................................')
    Packer.debug()



def exebutton(): 
    myString_TextureName()
    myString_Resolution_X_Name()
    myString_Resolution_Y_Name()
    myString_AlbedoSuffix()
    myString_NormalSuffix()
    myString_RoughnessSuffix()
    myString_MetalnessSuffix()
    myString_HeightSuffix()
    myString_AOSuffix()

    myString_Albedo()
    myString_Normal()
    myString_Roughness()
    myString_Metalness()
    myString_AO()
    myString_Height()
    
    Packer.convertimg()
    
    
#BUTTON
myButtonFindTextures = tk.Button(root, text='Find textures', command = myString_Find)
myButtonFindTextures.grid(row=3, column=0)


myButton = tk.Button(root, text='Convert', command = exebutton)
myButton.grid(row=103, column=0)


myButton = tk.Button(root, text='Debug', command = Packer.debug)
myButton.grid(row=104, column=0)




root.mainloop()



