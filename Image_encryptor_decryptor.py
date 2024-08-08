from PIL import Image 
import os
clear = lambda: os.system('cls')

def getImage():
    image = None
    
    while image == None:
        try:
            filename = input("Enter Image Name: ")
            image = Image.open(filename)
        except:
            print("[ERROR] Check Filename if file exist")
        
    return image
    

def encrypt():
    image = getImage()
    imageCopy =  image.copy()
    clear()
    print("====================================")
    print("Image Encryptor")
    print("====================================")
    key = None
    while key == None:
        try:
            key = int(input("Enter Key in Int: "))
        except:
            print("[ERROR] Key must be in int")
    
    pixel_map = image.load()
    pixel_mapCopy = imageCopy.load()
    width, height = image.size
            

    #flip color blue with red
    for i in range(0, width):
        for j in range(0, height):
            r, g, b, p = image.getpixel((i, j))
            b = (b ^ key) % 256
            r = (r ^ key) % 256
            g = (g ^ key) % 256
            pixel_map[i, j] = (b, g, r)
            
    
    #shift vertically       
    temp = 0
    for i in range(0, width):
        for j in range(0, height):
            y = ((j + temp * key) )%height
            pixel_mapCopy[i, y] = pixel_map[i, j]
        temp += i
    
    #shift horizontally   
    temp = 0
    for i in range(0, height):
        for j in range(0, width):            
            x = ((j + temp * key) )%width
            pixel_mapCopy[x, i] = pixel_map[j, i]
            
        temp += i
        

    
    imageCopy.save("encrypted.png") 

def decrypt():
    image = getImage()
    imageCopy =  image.copy()
    clear()
    print("====================================")
    print("Image Decryptor")
    print("====================================")
    
    key = None
    
    while key == None:
        try:
            key = int(input("Enter Key in Int: "))
        except:
            print("[ERROR] Key must be in int")
    
    pixel_map = image.load()
    pixel_mapCopy = imageCopy.load()
    width, height = image.size
            
    #flip color blue with red
    for i in range(0, width):
        for j in range(0, height):
            r, g, b, p = image.getpixel((i, j))
    
            b = (b ^ key) % 256
            r = (r ^ key) % 256
            g = (g ^ key) % 256
            pixel_map[i, j] = (b, g, r)
            
    #shift vertically    
    temp = 0
    for i in range(0, width):
        for j in range(0, height):
            y = ((j + temp * key) )%height
            pixel_mapCopy[i, j] = pixel_map[i, y]
        temp += i
    
    #shift horizontally 
    temp = 0
    for i in range(0, height):
        for j in range(0, width):            
            x = ((j + temp * key) )%width
            pixel_mapCopy[j, i] = pixel_map[x, i]
            
        temp += i
    
    imageCopy.save("decrypted.png") 


#main menu of the program that will ask user input on what action to do
def main():    
    while True:
        print("====================================")
        print("Image Security")
        print("====================================")
        print("[1] Encrypt")
        print("[2] Decrypt")
        print("[3] Exit")
        print("====================================")
        op1 = input("Option: ")
        
        if op1 == "1":
            encrypt()
        elif op1 == "2":
            decrypt()
        elif op1 == "3":
            print("Exit!")
            break
        else:
            clear()
            print("Invalid Input!!")
    
    
if __name__ == "__main__":
    main()