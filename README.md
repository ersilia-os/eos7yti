# Antimalarial activity from OSM

Scores triazolopyrazine analogues for antiplasmodial potency, trained by Ersilia on the roughly 400 Open Source Malaria Series 4 compounds whose IC50 values the consortium published as they were measured. Two LazyQSAR classifiers use activity cut-offs of 1 and 2.5 micromolar, reaching AUROC above 0.8 in cross-validation. Predictors from this campaign guided the generative rounds reported by Turon and colleagues, and of eight compounds eventually synthesised four were submicromolar. Coverage is deepest around Series 4 chemistry.

This model was incorporated on 2023-08-02.Last packaged on 2025-11-19.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7yti`
- **Slug:** `osm-series4`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Malaria`
- **Target Organism:** `Plasmodium falciparum`
- **Tags:** `Malaria`, `P.falciparum`, `IC50`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `2`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of Plasmodium falciparum inhibition at two IC50 cut-offs, 1 uM and 2.5 uM, reported separately.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| ic50_1um | float | high | Probability of inhibiting Pfalciparum measured as IC50 with a cut-off of 1uM |
| ic50_2point5um | float | high | Probability of inhibiting Pfalciparum measured as IC50 with a cut-off of 2.5uM |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7yti](https://hub.docker.com/r/ersiliaos/eos7yti)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7yti.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7yti.zip)

### Resource Consumption
- **Model Size (Mb):** `5`
- **Environment Size (Mb):** `7610`
- **Image Size (Mb):** `7499.4`

**Computational Performance (seconds):**
- 10 inputs: `61.7`
- 100 inputs: `60.34`
- 10000 inputs: `627.62`

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
