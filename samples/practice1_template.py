import sys
import cv2
import logging as log
import argparse
import array

sys.path.append('../src')
from imagefilter import ImageFilter

def build_argparse():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'your cmd argument', type = str)
    parser.add_argument('-g', '--isGrayscale', help = 'your cmd argument', type = str)
    
    #
    # Add your code here
    #
    
    return parser

def main():
    log.basicConfig(format="[ %(levelname)s ] %(message)s", level=log.INFO, stream=sys.stdout)
    log.info("Hello image filtering")
    args = build_argparse().parse_args()
    
    variable = args.input
    isGrayscale = args.isGrayscale
    log.info('nanana')
    
    image = cv2.imread(variable)
    if(isGrayscale)
        cvtColor(image,image,COLOR_RGBA2GRAY)
    width = image.shape[0]
    image[ : width //2 , :, :] = 0;
    image=cv2.resize(image, dsize  = (512,512))
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return
    
if __name__ == '__main__':         
    sys.exit(main())