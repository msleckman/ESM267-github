# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# uv-nc_to_s-tif.py
# Created on: 2018-09-28 10:56:17.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

verbose = True

# Import arcpy module
if verbose: print "import arcpy ..."
import arcpy
if verbose: print "...whew!"

arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

# Local variables:
u_nc = "H:\\ESM267\\lab1\\raw\\uwnd.sig995.2013.nc"
u_tmp = "u_tmp"
v_nc = "H:\\ESM267\\lab1\\raw\\vwnd.sig995.2013.nc"
v_tmp = "v_tmp"
s_tmp = "in_memory\\s_tmp"
# s_001_tif = "H:\\ESM267\\lab1\\out\\s_001.tif"

# loop over a range of values for j ( dont forget ":" after the 'for' statement)
for j in range(0, 365, 30):
    
    if verbose: print " day %d ..." %j
    
    # assign values based on variable j
    s_tif = "h:\\ESM267\\lab1\\out\\s_%03d.tif" % j
    print s_tif
    s_tmp = "in_memory\\s_%d" % j

    # Process: Make NetCDF Raster Layer
    arcpy.MakeNetCDFRasterLayer_md(u_nc, "uwnd", "lon", "lat", u_tmp, "", "time %d" % j, "BY_INDEX") # we put %d instead of %s because j is a number. J is inputed into a string, but the J itself is a umber

    # Process: Make NetCDF Raster Layer (2)
    arcpy.MakeNetCDFRasterLayer_md(v_nc, "vwnd", "lon", "lat", v_tmp, "", "time %d" % j, "BY_INDEX")

    # Process: Raster Calculator
    ## arcpy.gp.RasterCalculator_sa("SquareRoot( Square(\"%u_tmp%\") + Square(\"%v_tmp%\") )", s_tmp)
    arcpy.gp.RasterCalculator_sa("SquareRoot( Square('%s') + Square('%s') )" % (u_tmp, v_tmp), s_tmp)

    # Process: Resample
    arcpy.Resample_management(s_tmp, s_tif, "0.25 0.25", "BILINEAR")

