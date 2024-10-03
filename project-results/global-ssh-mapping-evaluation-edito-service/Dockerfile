FROM inseefrlab/onyxia-jupyter-pytorch:py3.11.10

COPY  ./dc_environment.yml ./env.yaml
RUN mamba env update -n base  -f ./env.yaml && \
    mamba clean --all --yes

USER 1000

EXPOSE 8888

CMD ["jupyter", "lab", "--no-browser", "--ip", "0.0.0.0"]
