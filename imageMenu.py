#encoding=utf-8

import sys
import os
import time
from PIL import ExifTags, Image
from effects import *
from filters import *


def run_option(path, option, im=None):
    """Runs choosen effect or filter option. Returns result of functions (allways an image, except for option 1)"""
    if im == None:
        im = prepare_image(path)

    ###########################################################################
    #                               THE MENU                                  #
    ###########################################################################

    ### EFFECTS ###

    if option == 1:
        """returns list of thumbnails with all effects and filters applied"""
        return (im, dic_thumbnails(im))

    elif option == 2:  # rotates images 90 degrees clockwise
        return rotate(im)

    elif option == 3:  # more contrast
        return contrast(im, 1.5)

    elif option == 4:  # less contrast
        return contrast(im, 0.5)

    elif option == 5:
        return saturation(im, 1.5)

    elif option == 6:
        return saturation(im, 0.5)

    elif option == 7:
        return luminosity(im, 1.5)

    elif option == 8:
        return luminosity(im, 0.8)

    elif option == 9:
        return change_2bpp(im)

    elif option == 10:
        return blur(im, 2)

    elif option == 11:
        return negative(im)

    elif option == 12:
        return black_white(im)

    elif option == 13:
        return sepia(im)

    elif option == 14:
        return is_edge(im, 17)

    ### FILTERS ###

    elif option == 21:
        return old_photo(im)

    elif option == 22:
        return pencil_draw(im)

    elif option == 23:
        return color_draw(im)

    elif option == 24:
        return circles_black(im)

    elif option == 25:
        return circles_white(im)
    
    ### CONTROLS ###

    # for use of stand alone simpleImageEditor.py
    elif option == 0:
        filename = str(time.time())+".jpg"
        im.save(filename, quality = 100)
        exit(0)

    # elif option == 30: NOT IMPLEMENTED, UNDO LAST OPTION
    #     return im

    else:
        print ("Wrong option. Option has to be a valid number")

#                                                                       #
##                             END MENU                                ##
#########################################################################


def dic_thumbnails(im):
    tn = []
    t = thumbnail(im)
    # append effects
    #tn.append({"crop": crop(t, 0, 0, 25, 25)})
    tn.append({"rotate": rotate(t)})
    tn.append({"moreContrast": contrast(t, 2)})
    tn.append({"lessContrast": contrast(t, 0.5)})
    tn.append({"moreSaturation": saturation(t, 2)})
    tn.append({"lessSaturation": saturation(t, 0.5)})
    tn.append({"moreLuminosity": luminosity(t, 2)})
    tn.append({"lessLuminosity": luminosity(t, 0.5)})
    tn.append({"change_2bpp": change_2bpp(t)})
    tn.append({"blur": blur(blur(t,2),2)})
    tn.append({"negative": negative(t)})
    tn.append({"blackWhite": black_white(t)})
    tn.append({"sepia": sepia(t)})
    tn.append({"isEdge": is_edge(t,17)})

    # append filterss
    tn.append({"oldPhoto": old_photo(t)})
    tn.append({"pencilDraw": pencil_draw(t)})
    tn.append({"colorDraw": color_draw(t)})
    tn.append({"circlesBlack": circles_black(t)})
    tn.append({"circlesWhite": circles_white(t)})

    return tn
def prepare_image(path):
    im = Image.open(path)
    width, height = im.size # by default (tags may exist, but not contain width and height)
    # tries to get correct width and height from image info
    try:
        tags = im._getexif()
        for k,v in tags.items():
            #print (str(ExifTags.TAGS[k])+" : "+str(v))
            if k == "ExifImageWidth":
                width = v
            if k == "ExifImageHeight":
                height = v
    except:
        pass

    # formats image to standard, if image does not meet project specifications and option is not to create thumbnails
    if (width/height) == (4/3) or (width/height) == (3/4):
        im = standard_format(im,1)
    else:
        im = standard_format(im,2)
    return im



if __name__ == "__main__":
    run_option(sys.argv[1], sys.argv[2])
