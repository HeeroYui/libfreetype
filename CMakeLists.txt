cmake_minimum_required(VERSION 2.8)

# Declare the project
project(freetype)

# set output path:
set(LIBRARY_OUTPUT_PATH lib/${CMAKE_BUILD_TYPE})

include_directories(.)

#Create src file list
set(src_files
	freetype/base/ftbbox.c
	freetype/base/ftbitmap.c
	freetype/base/ftglyph.c
	freetype/base/ftstroke.c
	freetype/base/ftxf86.c
	freetype/base/ftbase.c
	freetype/base/ftsystem.c
	freetype/base/ftinit.c
	freetype/base/ftgasp.c
	freetype/base/ftadvanc.c
	freetype/raster/raster.c
	freetype/sfnt/sfnt.c
	freetype/smooth/smooth.c
	freetype/autofit/autofit.c
	freetype/truetype/truetype.c
	freetype/cff/cff.c
	freetype/psnames/psnames.c
	freetype/pshinter/pshinter.c
)
set(inc_files
	freetype/ftcache.h
	freetype/fttypes.h
	freetype/ftgxval.h
	freetype/ftchapters.h
	freetype/fterrors.h
	freetype/tttags.h
	freetype/smooth/ftgrays.h
	freetype/smooth/ftsmerrs.h
	freetype/smooth/ftsmooth.h
	freetype/ftadvanc.h
	freetype/ftbitmap.h
	freetype/ftcid.h
	freetype/ftoutln.h
	freetype/ftimage.h
	freetype/ftmodapi.h
	freetype/ftotval.h
	freetype/ttnameid.h
	freetype/ftsystem.h
	freetype/cff/cffobjs.h
	freetype/cff/cfftoken.h
	freetype/cff/cffload.h
	freetype/cff/cffdrivr.h
	freetype/cff/cffparse.h
	freetype/cff/cfftypes.h
	freetype/cff/cffgload.h
	freetype/cff/cffcmap.h
	freetype/cff/cfferrs.h
	freetype/freetype.h
	freetype/config/ftmodule.h
	freetype/config/ftheader.h
	freetype/config/ftconfig.h
	freetype/config/ftstdlib.h
	freetype/config/ftoption.h
	freetype/ftsizes.h
	freetype/ftsynth.h
	freetype/ftlzw.h
	freetype/ft2build.h
	freetype/ftgzip.h
	freetype/psaux/psconv.h
	freetype/psaux/t1cmap.h
	freetype/psaux/psauxmod.h
	freetype/psaux/psobjs.h
	freetype/psaux/afmparse.h
	freetype/psaux/psauxerr.h
	freetype/psaux/t1decode.h
	freetype/truetype/ttpload.h
	freetype/truetype/tterrors.h
	freetype/truetype/ttobjs.h
	freetype/truetype/ttgxvar.h
	freetype/truetype/ttinterp.h
	freetype/truetype/ttgload.h
	freetype/truetype/ttdriver.h
	freetype/ftglyph.h
	freetype/autofit/afhints.h
	freetype/autofit/aflatin.h
	freetype/autofit/afcjk.h
	freetype/autofit/aftypes.h
	freetype/autofit/aflatin2.h
	freetype/autofit/afdummy.h
	freetype/autofit/afglobal.h
	freetype/autofit/afloader.h
	freetype/autofit/afmodule.h
	freetype/autofit/afindic.h
	freetype/autofit/afwarp.h
	freetype/autofit/afangles.h
	freetype/autofit/aferrors.h
	freetype/ftgasp.h
	freetype/ftmm.h
	freetype/ftlist.h
	freetype/ftlcdfil.h
	freetype/t1tables.h
	freetype/ftincrem.h
	freetype/ftstroke.h
	freetype/ftbdf.h
	freetype/ft2unix.h
	freetype/ftrender.h
	freetype/ftmac.h
	freetype/ftxf86.h
	freetype/ftmoderr.h
	freetype/tttables.h
	freetype/internal/ftdebug.h
	freetype/internal/ftrfork.h
	freetype/internal/pcftypes.h
	freetype/internal/ftserv.h
	freetype/internal/ftdriver.h
	freetype/internal/ftobjs.h
	freetype/internal/ftstream.h
	freetype/internal/internal.h
	freetype/internal/pshints.h
	freetype/internal/ftgloadr.h
	freetype/internal/ftcalc.h
	freetype/internal/t1types.h
	freetype/internal/psaux.h
	freetype/internal/sfnt.h
	freetype/internal/autohint.h
	freetype/internal/tttypes.h
	freetype/internal/ftvalid.h
	freetype/internal/services/svpscmap.h
	freetype/internal/services/svbdf.h
	freetype/internal/services/svxf86nm.h
	freetype/internal/services/svgldict.h
	freetype/internal/services/svpostnm.h
	freetype/internal/services/svwinfnt.h
	freetype/internal/services/svgxval.h
	freetype/internal/services/svttglyf.h
	freetype/internal/services/svpsinfo.h
	freetype/internal/services/svmm.h
	freetype/internal/services/svttcmap.h
	freetype/internal/services/svcid.h
	freetype/internal/services/svkern.h
	freetype/internal/services/svpfr.h
	freetype/internal/services/svtteng.h
	freetype/internal/services/svotval.h
	freetype/internal/services/svsfnt.h
	freetype/internal/fttrace.h
	freetype/internal/ftmemory.h
	freetype/fttrigon.h
	freetype/sfnt/sferrors.h
	freetype/sfnt/ttpost.h
	freetype/sfnt/ttbdf.h
	freetype/sfnt/ttkern.h
	freetype/sfnt/sfobjs.h
	freetype/sfnt/sfdriver.h
	freetype/sfnt/ttmtx.h
	freetype/sfnt/ttsbit.h
	freetype/sfnt/ttcmap.h
	freetype/sfnt/ttload.h
	freetype/fterrdef.h
	freetype/raster/ftrend1.h
	freetype/raster/rasterrs.h
	freetype/raster/ftraster.h
	freetype/raster/ftmisc.h
	freetype/ftpfr.h
	freetype/ttunpat.h
	freetype/ftbbox.h
	freetype/ftsnames.h
	freetype/pshinter/pshglob.h
	freetype/pshinter/pshmod.h
	freetype/pshinter/pshalgo.h
	freetype/pshinter/pshrec.h
	freetype/pshinter/pshnterr.h
	freetype/ftwinfnt.h
	freetype/psnames/psnamerr.h
	freetype/psnames/psmodule.h
	freetype/psnames/pstables.h
)

add_definitions( -W )
add_definitions( -Wall )
add_definitions( -DPIC )
add_definitions( -DDARWIN_NO_CARBON )
add_definitions( -DFT2_BUILD_LIBRARY )
add_definitions( -DANDROID_FONT_HACK=1 )

#Create a static Lib:
add_library(freetype STATIC ${src_files} ${inc_files} )

