from PIL import Image, ImageDraw
from SortFunctions import selectionSort
from SearchFunctions import binarySearch


def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]


# end def comparePixels(pix1,pix2):


def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store ppixels inout double tuple format.
    pixel_array = []

    for i in range(width):  # for loop for x position
        for j in range(height):  # for loop for y position
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))
            pixel_array.append([(r, g, b), (i, j)])
        # end for j
    # end for i
    return pixel_array


# end def storePixels(im):

def main():
    IMG_NAME = 'panda'

    # open image
    # read each pixel into memory as the image object im
    with Image.open(IMG_NAME + '.jpeg') as im:
        pixels = storePixels(im)

    # TODO
        # sort copy of pixles
        selectionSort(pixels, comparePixels)
        #search copy for r
        binarySearch(pixels, 0, len(pixels)-1, r)
        # grayscale pixels
        # restore found r

    # end with Image.open(IMG_NAME + '.jpg') as im:

    # save my image data from memory to a file with a different name
    im.save('neg_' + IMG_NAME + '.jpeg', 'JPEG')

    # opens with your external preiview program, shows memory representaion
    im.show()


# end of def main():

if __name__ == "__main__":
    main()
