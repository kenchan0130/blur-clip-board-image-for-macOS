#!/usr/bin/env python

import objc
import sys
import os.path
import ctypes.util
import collections
from AppKit import NSPasteboard, NSImage, NSBitmapImageRep, NSPasteboardTypeTIFF
from Quartz.CoreGraphics import CGRectMake


def loadObjcFramework(framework_name):
    loaded_classes = dict()
    framework_bundle = objc.loadBundle(framework_name, bundle_path=os.path.dirname(
        ctypes.util.find_library(framework_name)), module_globals=loaded_classes)
    return collections.namedtuple(
        'AttributedFramework',
        loaded_classes.keys())(
        **loaded_classes)


def main():
    blur_rate = 8.5
    if len(sys.argv) > 2:
        blur_rate = float(sys.argv[1])
    
    core_image = loadObjcFramework('CoreImage')
    paste_board = NSPasteboard.generalPasteboard()
    image_data = paste_board.dataForType_(NSPasteboardTypeTIFF)
    
    if image_data is None:
        print("Not found image data in clip borad.")
        sys.exit(1)
    
    ci_clipboard_image = core_image.CIImage.imageWithData_(image_data)
    filter = core_image.CIFilter.filterWithName_('CIGaussianBlur')
    filter.setDefaults()
    filter.setValue_forKey_(ci_clipboard_image, "inputImage")
    filter.setValue_forKey_(blur_rate, "inputRadius")

    ci_clipboard_image_size = ci_clipboard_image.extent().size
    output_image = filter.outputImage()
    bitmap_image = NSBitmapImageRep.alloc().initWithCIImage_(output_image.imageByCroppingToRect_(CGRectMake(0 , 0, ci_clipboard_image_size.width, ci_clipboard_image_size.height)))

    paste_board.clearContents()
    paste_board.setData_forType_(bitmap_image.TIFFRepresentation(), NSPasteboardTypeTIFF)
    
    print("Done.")