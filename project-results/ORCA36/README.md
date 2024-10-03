# ORCA36 validation project

## To-do list

 - [x] learn how to connect to a personnal git repository in the edito platform
 - [x] learn how to access ORCA36 data (concatenate the whole year of surface fields in one dataarray)
 - [x] learn how to access DUACS, OSTIA and GLOBCURRENT
 - [ ] compute annual mean and standart deviation for
   - [ ] SSH in ORCA36
   - [ ] SSH in AVISO
   - [x] SST in ORCA36
   - [x] SST in OSTIA
   - [ ] EKE from SSU SSV from ORCA36
   - [ ] EKE from SSU SSV from GLOBCURRENT
and save them in netcdf files
- [ ] make nice comparison plots !
- [x] Define regions
  - [x] Gulf Stream 
  - [x] Kuroshio 
  - [x] Aguilhas
  - [x] California 

```
domain=[[20,40,-140,-105],[25,43,-82,-50],[25,45,130,160],[-50,-30,15,50]] # [Lat0,Lat1,Lon0,Lon1]
region=("California Current","Gulf Stream","Kuroshio Current","Agulhas Current")
```