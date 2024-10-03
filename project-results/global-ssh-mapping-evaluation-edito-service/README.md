# Results

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
