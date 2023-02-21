from PIL import Image;
from colorama import Fore, Back, Style

# RED Channel = AOA
# Green Channgel = Rougness
# Blue Channel = Metallic

print(Fore.CYAN+ '''
 ___   __   __  _______  _______  _______  _______  ______   
|   | |  |_|  ||       ||       ||       ||  _    ||    _ |  
|   | |       ||    ___||____   ||    _  || |_|   ||   | ||  
|   | |       ||   | __  ____|  ||   |_| ||       ||   |_||_ 
|   | |       ||   ||  || ______||    ___||  _   | |    __  |
|   | | ||_|| ||   |_| || |_____ |   |    | |_|   ||   |  | |
|___| |_|   |_||_______||_______||___|    |_______||___|  |_|
''' + Fore.RESET)

heart = (Fore.RED + "<3" + Fore.RESET)
print("Create PBR images for Microsoft Flight Simulator by merging AOA,Roughness and Metallic into a single image! ;) \n")
print("Made with " + heart + " by Unai González (@unaiitxuu) \n")
images = input('''Insert the images in this order separated by a space: 

Example: "Concrete01_AO.png Concrete01_RG.png Concrete01_MT.png"

''' + Fore.RED +  '''1. Red Channel = AOA \n'''
 + Fore.GREEN + '''2. Green Channgel = Rougness\n''' +
Fore.BLUE + '''3. Blue Channel = Metallic : ''' + Fore.RESET)

print("")

images_splitted = images.split()

red_image = images_splitted[0]
green_image = images_splitted[1]
blue_image = images_splitted[2]

def IMG2PBR(red_image1, green_image1, blue_image1):
    red_channel = Image.open(red_image1);
    filename = red_channel.filename;
    red_channel = Image.open(red_image1).convert('L');
    green_channel = Image.open(green_image1).convert('L');
    blue_channel = Image.open(blue_image1).convert('L');
    rgb = Image.merge("RGB",(red_channel,green_channel,blue_channel));
    rgb.save(filename[:-4] + "_PBR.png")
    print("Done! Your PBR image is saved as: " + filename[:-4] + "_PBR.png");

IMG2PBR(red_image,green_image,blue_image)





