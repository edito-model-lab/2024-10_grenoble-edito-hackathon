# The Global SSH Mapping Data Challenge EDITO (GMS-DC-Edito) service

The specific goal of the European Digital Twin Ocean (EDITO) platform and infrastructures is to allow users to
explore and share ocean data, models and services in an open and collaborative way. In this spirit, the EDITO platform and the Ocean Data Challenges initiative fully align and benefit each other. 

Here, the GMS-DC-Edito service aims at providing automated evaluation for the 2023 conventional nadir altimetry mapping data challenge: [2023a_SSH_mapping_OSE](https://github.com/ocean-data-challenges/2023a_SSH_mapping_OSE).


![Capture d’écran 2024-10-03 à 11 50 06](https://github.com/user-attachments/assets/f138617c-0e28-4668-8056-e5ececbfc1a7)



## How to use the GMS-DC-Edito service

- Make your maps accessible with a downloading url,

- Log in to the Edito Platform and select the GMS-DC-Edito service,

- Insert name of the method and downloading url as variables to the GMDC-Edito service,

- Run the service which will launch the appropriate docker image, download the evaluation data, clone the data challenge repo and run the three evaluation notebooks (ssh_scores, uv_scores and uv_traj) and display them.


## Results

What has been done during the hackathon:

- building a docker image with the environment see `Dockerfile` and `env.yml`
- scripting the evaluation notebooks execution see branch `Run_DC_on_Edito` of `https://github.com/ocean-data-challenges/2023a_SSH_mapping_OSE.git`
- scripting the data download: see `download_and_access_global_data.ipynb`
- writing a configurable init_script: see init_script.sh

- putting it all together in preconfigured jupyter service:
```
 https://datalab.dive.edito.eu/launcher/ide/jupyter-pytorch?name=global-eval-w-env&version=2.1.4&autoLaunch=true&service.image.custom.enabled=true&service.image.custom.version=«quentinf00%2F2023-dc-env%3Av0»&resources.limits.cpu=«1900m»&resources.limits.memory=«16Gi»&persistence.size=«35Gi»&init.personalInit=«https%3A%2F%2Fminio.lab.dive.edito.eu%2Foidc-quentinfebvre%2Finit_script.sh»&init.personalInitArgs=«4dvarnet%20https%3A%2F%2Fminio.lab.dive.edito.eu%2Foidc-dzhu%2Fmappings-4dvarnet%2Foutput.nc»
```

- Investigating how to deploy a proper service/process on edito see `Chart.yml`


## The future of evaluation: coming soon

The next steps will be to automate the GMDC-Edito steps described above initially launched by a GitHub action. 

The first trigger would be a pull request by the user containing a config file with both a method name and a downloading url. 
From there, several GitHub actions will launch the GMDC-Edito service in the background which will end by a github push of the three new (appropriately named) notebooks onto the Global Mapping Data Challenge repository. 

In a nutshell, the data challenge participant will make a pull request for its maps and several minutes later will see the performances of its method appear online. 


## First results,
In order to have a first notebook generated with the service, we ran a smaller service with only alongtrack comparison on a coarsen 4dvarnet map
the service ran is with the service

https://datalab.dive.edito.eu/launcher/ide/jupyter-pytorch?name=global-eval-w-env&version=2.1.4&autoLaunch=true&service.image.custom.enabled=true&service.image.custom.version=«quentinf00%2F2023-dc-env%3Av0»&resources.limits.cpu=«1900m»&resources.limits.memory=«16Gi»&persistence.size=«35Gi»&init.personalInit=«https%3A%2F%2Fminio.lab.dive.edito.eu%2Foidc-quentinfebvre%2Finit_script_alti_only.sh»&init.personalInitArgs=«4dvarnet_coarse%20https%3A%2F%2Fminio.lab.dive.edito.eu%2Foidc-dzhu%2Fmappings-4dvarnet%2F4dvarnet_coarse.nc» 

and the generated notebook is ssh_scores_4dvarnet_coarse_edito.ipynb

