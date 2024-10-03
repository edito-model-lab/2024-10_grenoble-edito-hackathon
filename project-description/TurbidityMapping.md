
## Title 
### TurbidityMapping

## Short description of the project 
Create a pipeline for performing turbidity mapping using a pre-trained 4dvarnet model
over Wadden Sea region which contains Dutch Wadden Sea and German Wadden Sea.

Integrate Inference for pretrained 4DVarNet-based 

## Expected benefit of the project
Create a service for turbidity Mapping and analysing evaluation metrics and visualiations. 
This inference allows us to benchmark the model agaist a classical method called Dineof
with the ML based 4dvarnet.

## Datasets
- Dataset is provided by CMEMS services, it is also uploaded on EDITO cloud
- A pretrained weight is uploaded on EDITO cloud as well

## Codebase
Description of the software packages that will be used (with links to github repos): https://github.com/nguyenthuynga/4dvarnet-starter

## Compute resources 
4DVarNet model training and inference needs heavy computation, and since the current GPU resources limit our inference to a month of data instead of the whole year at one. 
We will require H100 GPU for performing training/inference in the future.    

## People involved 
List of people involved: Fabio, Minh, Nga, Shashank
