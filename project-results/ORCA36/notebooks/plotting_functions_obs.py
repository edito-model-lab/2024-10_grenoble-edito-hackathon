import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cmocean
import numpy as np

def map_mean_GS_obs(data,lon,lat,domain,title,unit,vmin,vmax,cmap,name):
    """
    Produces a map of a 2D field for not regular grid (lon and lat are 2D)
    """

    min_lonGS = np.array(domain[2])
    min_latGS = np.array(domain[0])
    max_lonGS = np.array(domain[3])
    max_latGS =  np.array(domain[1])

    fig=plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111,projection=ccrs.PlateCarree())
    
    pcolor=ax.pcolormesh(lon,lat,data,cmap=cmap,vmin=vmin,vmax=vmax,transform=ccrs.PlateCarree())
    ax.set_extent([min_lonGS, max_lonGS, min_latGS+2, max_latGS-2])
    
    ax.add_feature(cfeature.LAND,facecolor='grey')
    ax.coastlines()
    gl=ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,linewidth=2, color='gray', alpha=0.5, linestyle='--')
    
    fig.subplots_adjust(right=0.8)
    gl.xlocator = mticker.FixedLocator(np.arange(-180,179,5))
    gl.ylocator = mticker.FixedLocator(np.arange(-80,80,5))
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 15, 'color': 'black'}
    gl.ylabel_style = {'size': 15, 'color': 'black'}
    
    cbar = plt.colorbar(pcolor,orientation='vertical',shrink=0.75,label=unit)
    ax.set_title(title,size=15,y=1.05)
    plt.savefig(name)
    