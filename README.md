# Antimalarial activity from OSM

This model predicts the antimalarial potential of small molecules in vitro. We have collected the data available from the Open Source Malaria Series 4 molecules and used two cut-offs to define activity, 1 uM and 2.5 uM. The training has been done with the LazyQSAR package (CheMeleon embeddings) and shows an AUROC >0.8 in a 3-fold cross-validation on 25% of the data held out as test. These models have been used to generate new series 4 candidates by Ersilia.

This model was incorporated on 2023-08-02.Last packaged on 2025-07-30.

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
- **Interpretation:** Probability of killing P.falciparum in vitro (IC50 < 1uM and 2.5uM, respectively)

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
- **Model Size (Mb):** `7`
- **Environment Size (Mb):** `7880`
- **Image Size (Mb):** `6464.21`

**Computational Performance (seconds):**
- 10 inputs: `54.7`
- 100 inputs: `61.86`
- 10000 inputs: `541.72`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-qsar](https://github.com/ersilia-os/lazy-qsar)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acsmedchemlett.4c00131](https://pubs.acs.org/doi/10.1021/acsmedchemlett.4c00131)
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
