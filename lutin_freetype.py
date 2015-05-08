#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "FreeType lib (generate font with true type file)"


def create(target):
	myModule = module.Module(__file__, 'freetype', 'LIBRARY')
	
	#remove compilation warning (specific for external libs):
	myModule.remove_compile_warning()
	
	myModule.add_src_file([
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
	
	myModule.compile_flags('c', [
		'-W',
		'-Wall',
		'-DPIC',
		'-DDARWIN_NO_CARBON',
		'-DFT2_BUILD_LIBRARY',
		'-DANDROID_FONT_HACK=1'])
	
	myModule.add_export_path(tools.get_current_path(__file__))
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/internal")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/internal/services")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/psaux")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/pshinter")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/psnames")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/raster")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/sfnt")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/smooth")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/truetype")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/autofit")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/base")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/cff")
	myModule.add_path(tools.get_current_path(__file__)+"/freetype/config")
	
	myModule.compile_version_CC(1999)
	
	# add the currrent module at the 
	return myModule
	

