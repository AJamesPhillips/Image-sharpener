
import matplotlib.pyplot as plt     #    http://matplotlib.sourceforge.net/api/pyplot_api.html
import matplotlib.image as mpimg    #    
import numpy as np
#import scipy.misc as scm

def imageSharpen (filename, fileExtension):
    image = mpimg.imread('../input images/' + filename + fileExtension)
    #note image will be a 3 dimensional array
    # the first axis is y, going up, 2nd is x, going to 
    # the right, and the third is the RGB component.
    # When the results is then produced by plt.imshow, 
    # will need to set origin to 'lower' 
    
    #remove the alpha channel (if present)
    image = np.compress([1,1,1,0],image,axis=2)
    
    
    
    filterWidth = 3
    filterHeight = 3;
    width = image.shape[1];
    height = image.shape[0];
    
    filter = np.ones([filterWidth, filterHeight]) * -1
    filter[1,1] = 9
    
    factor = 1.0;
    bias = 0.0;
    
    result = np.empty_like(image);
    
    for x in range(width):
      for y in range(height):
        red = 0.0
        green = 0.0
        blue = 0.0
        
        for filterX in range(filterWidth):
          for filterY in range(filterHeight):
            imageX = (x - filterWidth / 2 + filterX + width) % width
            imageY = (y - filterHeight / 2 + filterY + height) % height
            
            imageColor = image[imageY,imageX]
            red += imageColor[0] * filter[filterX, filterY]
            green += imageColor[1] * filter[filterX, filterY]
            blue += imageColor[2] * filter[filterX, filterY]
        
        red = min(max(red*factor+bias,0),255)
        green = min(max(green*factor+bias,0),255)
        blue = min(max(blue*factor+bias,0),255)
          
        result[y,x] = [red,green,blue]
    
    plt.imshow(result, origin='lower')
    plt.savefig('../processed images/' + filename + '.jpeg')
    #scm.imsave('../processed images/' + filename + fileExtension, result)

    
imageSharpen("image", ".bmp")

