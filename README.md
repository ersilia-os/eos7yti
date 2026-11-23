# Antimalarial activity from OSM

Scores triazolopyrazine analogues for antiplasmodial potency. Ersilia trained two LazyQSAR classifiers on 413 Open Source Malaria Series 4 compounds, with IC50 cut-offs of 1 and 2.5 micromolar (123 and 175 actives), reaching AUROC 0.89 and 0.87 in five-fold out-of-fold validation. Outputs are ranks against 50,000 drug-like molecules. Predictors from this campaign guided generative rounds in which four of eight synthesised compounds were submicromolar. Coverage is deepest around Series 4 chemistry.

This model was incorporated on 2023-08-02.
Last packaged on 2026-11-23.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7yti`
- **Slug:** `osm-series4`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Malaria`
- **Target Organism:** `Plasmodium falciparum`
- **Tags:** `Antiparasitic activity`, `IC50`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Rank of predicted Plasmodium falciparum inhibition at IC50 cut-offs of 1 uM and 2.5 uM, against 50,000 drug-like molecules; 0.65 is better than 99% of them.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| ic50_1um_rank | float | high | Rank score of the compound's predicted inhibition of Plasmodium falciparum at an IC50 cut-off of 1 uM, calibrated against a reference library of 50K drug-like molecules so that 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| ic50_2point5um_rank | float | high | Rank score of the compound's predicted inhibition of Plasmodium falciparum at an IC50 cut-off of 2.5 uM, calibrated against a reference library of 50K drug-like molecules so that 0.65 is better than 99% of them. Recommended threshold: 0.65. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7yti](https://hub.docker.com/r/ersiliaos/eos7yti)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7yti.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7yti.zip)
- **Apptainer**: [https://models-sif.s3.eu-north-1.amazonaws.com/eos7yti_v3.sif](https://models-sif.s3.eu-north-1.amazonaws.com/eos7yti_v3.sif)

### Resource Consumption
- **Model Size (Mb):** `27`
- **Environment Size (Mb):** `6954`
- **Image Size (Mb):** `3289.13`

**Computational Performance (seconds):**
- 10 inputs: `36.15`
- 100 inputs: `29.39`
- 10000 inputs: `290.95`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-qsar](https://github.com/ersilia-os/lazy-qsar)
- **Publication**: [https://doi.org/10.1021/acsmedchemlett.4c00131](https://doi.org/10.1021/acsmedchemlett.4c00131)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7yti
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7yti
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
