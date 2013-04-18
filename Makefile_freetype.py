#!/usr/bin/python
#for freetype : https://github.com/cdave1/freetype2-android

import module
import buildTools

myModule = module.module(__file__, 'freetype', 'LIBRARY')

myModule.AddSrcFile([
	'freetype/base/ftbbox.c',
	'freetype/base/ftbitmap.c',
	'freetype/base/ftglyph.c',
	'freetype/base/ftstroke.c',
	'freetype/base/ftxf86.c',
	'freetype/base/ftbase.c',
	'freetype/base/ftsystem.c',
	'freetype/base/ftinit.c',
	'freetype/base/ftgasp.c',
	'freetype/base/ftadvanc.c',
	'freetype/raster/raster.c',
	'freetype/sfnt/sfnt.c',
	'freetype/smooth/smooth.c',
	'freetype/autofit/autofit.c',
	'freetype/truetype/truetype.c',
	'freetype/cff/cff.c',
	'freetype/psnames/psnames.c',
	'freetype/pshinter/pshinter.c'])

myModule.CompileFlags_CC([
	'-W',
	'-Wall',
	'-DPIC',
	'-DDARWIN_NO_CARBON',
	'-DFT2_BUILD_LIBRARY',
	'-DANDROID_FONT_HACK=1'])

myModule.AddExportPath(buildTools.GetCurrentPath(__file__))
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/internal")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/internal/services")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/psaux")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/pshinter")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/psnames")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/raster")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/sfnt")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/smooth")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/truetype")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/autofit")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/base")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/cff")
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/freetype/config")

# add the currrent module at the 
module.AddModule(myModule)


