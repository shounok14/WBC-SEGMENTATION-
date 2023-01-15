# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:45:57 2022

@author: rishikroy
"""
from PIL import Image,ImageEnhance,ImageFilter
class Main:
     def caller_func(self):
         #self parameter is a reference to the current instance of the class Main & it's used to access the funcs and vars of Main
         f = 0
         print("WBC Detection from blood-smear images")
         print("\t\tdeveloped through PIL in Python")
         op = Operations()
         while(1):
            print("\nOperations Menu:-\n")
            print("a. Perform Preprocessing on the image")
            print("b. Perform Thresholding of the image")
            print("c. Perform Edge-Detection on the given image")
            print("d. Quit operations")
            ch = input("\n Please enter any one - ")
            if ch == "a":
               print("Performing Preprocessing of the image ->")
               op.rgb_grayscale()
            elif ch == "b":
               print("Running Thresholding Operation on the image ->")
               op.threshold()
            elif ch == "c":
               print("Running edge-detection on the image ->")
               op.edge_detect()
            else:
               print("Quitting Operations.."+exit())
            f+=1
            if f >= 3:
               break
         return 0

class Operations:
    def rgb_grayscale(self):
      im = Image.open(r'C:\Users\rikk2\OneDrive\Pictures\Saved Pictures\cell3.jpg')
      # A new image object is being created in 'RGB' mode; also given RGB factor values respectively 
      mod_im = Image.new('RGB', im.size,(25,10,2))
      # pastes the image into the new one after the splittng the RGB bands from the original img
      mod_im.paste(im,im.split()[2]) 
      mod_im.show()
      # applying grayscale method using convert() with parameter 'L'
      im = mod_im.convert('L')
      im.show()
      im = im.save('cell_greyscale.jpg')
      return 0

    def threshold(self):
     # Method to process the red band
     def pixProcess_R(intensity):
         return 0
     # Method to process the green band
     def pixProcess_G(intensity):
         return intensity
     # Method to process the blue band
     def pixProcess_B(intensity):
         return 0 
     # Create an image object
     img  = Image.open(r'C:\Users\rikk2\OneDrive\Pictures\Saved Pictures\cell3.jpg')
     # Split the red, green and blue bands from the Image in variable mulband
     mulband  = img.split()

     # Apply point operations that does thresholding on each color band
     redband = mulband[0].point(pixProcess_R)
     greenband = mulband[1].point(pixProcess_G)
     blueband = mulband[2].point(pixProcess_B)

     # Display the individual band after thresholding
     redband.show()
     blueband.show()
     greenband.show()

     # Create a new image from the thresholded red, green and blue brands
     mod_img = Image.merge("RGB", (redband, greenband, blueband))

     # Display the merged image after thresholding
     mod_img.show()
     return 0

    def edge_detect(self):
      filename = r'cell_greyscale.jpg'
      img = Image.open(filename)
      enh = ImageEnhance.Brightness(img)
      # Enhancing the brightness factor by 2.5
      img = enh.enhance(2)
      enh = ImageEnhance.Sharpness(img)
      # Enhancing the sharpness factor by 2.5
      img = enh.enhance(2)
      img = img.filter(ImageFilter.FIND_EDGES)
      # Edge Detect Operation for the enhanced image
      enh = ImageEnhance.Color(img)
      # colour modulation for the edge-detected image
      img = enh.enhance(-0.77)
      img.show()
      return 0

#Creating an instance of the class Main and using it to access its other members 
main = Main()
main.caller_func()    