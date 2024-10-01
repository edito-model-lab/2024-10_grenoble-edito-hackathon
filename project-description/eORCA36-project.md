# Template for describing the hackathon projects 

## Title 
ORCA36 validation with satellite products

## Short description of the project 

Comparison of surface fields of temperature, velocities between ORCA36 simulation outputs and satellite products available on the edito platform.
We will focus on some key regions : Gulf Stream, Aguilhas, Kuroshio, California and maybe Circumpolar region if available in the data
We will try to ook at annual mean and standart deviation
If time, computation and comparison of EKE 

## Expected benefit of the project
Quick validation of ORCA36 simuation outputs and introduction for us to the platform and accessing the data

## Datasets
ORCA36 simulation provided by Clément Bricaud (MOI)
DUACS SSH product
OSTIA SST product
GLOBCURRENT product

All of them already on edito platform

## Codebase

xarray, zarr, cartopy, matplotlib, numpy

## Compute resources 
The computation of mean and standart deviation in regional area will need some significant ressources 
For the ORCA36 outputs we will focus on regions that are 1000x2000x24x365
The maximum number CPU and at least 20Gb of RAM will be needed

## People involved 
Marcela Contreras & Aurélie Albert (IGE)
