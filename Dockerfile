FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2023.3.2
RUN pip install joblib
RUN pip install git+https://github.com/ersilia-os/lazy-qsar.git@b930abc17da7b2c18be1ad48440593ca7a6edbf3

WORKDIR /repo
COPY . /repo
