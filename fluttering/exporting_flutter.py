
import xarray as xr
import cartopy.crs as ccrs

from pathlib import Path
import flutter

dir_data = Path("data/reduced")
dir_fig = Path("data/fig")
dir_vid = dir_fig/ "vid"

da = xr.load_dataset(dir_data/"hundred_members_2t_pf.nc")
da = da.assign_coords({"longitude": [ i if i <= 180 else i-360 for i in da.longitude.values]})
# reduce spatial range
da = da.sel(longitude=slice(-20,20),latitude=slice(65,35))




# Es=[50]
Es=[50,100] 
# Es=[10,20,50,100]

timesteps = 5
Ts = range(0,11,11//timesteps)

n_repetitions = 2
shuffle = True

temp_threshold = 268
# temp_threshold = 273.15 
params_temp = dict(vmin=250, vmax=290)


for E in Es:
    flutter.export_flutter(da,Ts,E,
            filename=dir_vid/f"ensembles_time_subfreezing_T{timesteps}_{E}.mp4",
            projection= ccrs.PlateCarree(),
            transform = ccrs.PlateCarree(),
            plot_params=params_temp,
            threshold=temp_threshold,
            n_repetitions=n_repetitions, shuffle=shuffle,
            title=f"Temperatures <-5⁰C N_ens:{E:3}"
            )