#!/bin/bash


wget https://minio.lab.dive.edito.eu/oidc-quentinfebvre/download_and_acces_global_data.ipynb

git clone --depth 1 -b Run_DC_on_Edito https://github.com/ocean-data-challenges/2023a_SSH_mapping_OSE 
cd 2023a_SSH_mapping_OSE
papermill -k python3  ../download_and_acces_global_data.ipynb ../output.ipynb -p method $1 -p url $2
ln -s ../data data

cd nb_diags_global

papermill -k python3 ssh_scores_template.ipynb -p method_name $1 -p method_path ../$1.nc ssh_scores_$1_edito.ipynb
papermill -k python3 uv_scores_template.ipynb -p method_name $1 -p method_path ../$1.nc uv_scores_$1_edito.ipynb
papermill -k python3 uv_traj_template.ipynb -p method_name $1 -p method_path ../$1.nc uv_traj_$1_edito.ipynb
