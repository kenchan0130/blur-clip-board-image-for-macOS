#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
from AppKit import NSPasteboard, NSImage, NSBitmapImageRep, NSPasteboardTypeTIFF
from Quartz.CoreGraphics import CGRectMake
from Quartz import CIImage, CIFilter


def parseArgs():
    parser = argparse.ArgumentParser(description='Command line tool for blur processing of image for macOS')
    default_blur_rate = 8.5
    parser.add_argument("-r", "--rate",
                    help="blur rate, default %s" % default_blur_rate,
                    default=8.5,
                    type=float)
    args = parser.parse_args()

    return args


def getImageDataFromClipBoard(paste_board):
    image_data = paste_board.dataForType_(NSPasteboardTypeTIFF)
    
    if image_data is None:
        print >> sys.stderr, "Not found image data in clip borad."
        sys.exit(1)
    
    return image_data


def main():
    args = parseArgs()
    blur_rate = args.rate

    paste_board = NSPasteboard.generalPasteboard()
    image_data = getImageDataFromClipBoard(paste_board)
    
    ci_clipboard_image = CIImage.imageWithData_(image_data)
    filter = CIFilter.filterWithName_('CIGaussianBlur')
    filter.setDefaults()
    filter.setValue_forKey_(ci_clipboard_image, "inputImage")
    filter.setValue_forKey_(blur_rate, "inputRadius")

    ci_clipboard_image_size = ci_clipboard_image.extent().size
    output_image = filter.outputImage()
    bitmap_image = NSBitmapImageRep.alloc().initWithCIImage_(output_image.imageByCroppingToRect_(CGRectMake(0 , 0, ci_clipboard_image_size.width, ci_clipboard_image_size.height)))

    paste_board.clearContents()
    paste_board.setData_forType_(bitmap_image.TIFFRepresentation(), NSPasteboardTypeTIFF)
    
    print("Done.")


if __name__ == "__main__":
    main()