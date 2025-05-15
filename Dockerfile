FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*
RUN pip install rdkit==2023.3.2
RUN pip install joblib==1.5.0
RUN pip install git+https://github.com/ersilia-os/lazy-qsar.git@b930abc17da7b2c18be1ad48440593ca7a6edbf3
RUN pip install scikit-learn==1.2.2

WORKDIR /repo
COPY . /repo
