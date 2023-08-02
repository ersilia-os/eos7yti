# Antimalarial activity from OSM

This model predicts the antimalarial potential of small molecules in vitro. We have collected the data available from the Open Source Malaria Series 4 molecules and used two cut-offs to define activity, 1 uM and 2.5 uM. The training has been done with the LazyQSAR package (Morgan Binary Classifier) and shows an AUROC >0.8 in a 5-fold cross-validation on 20% of the data held out as test. These models have been used to generate new series 4 candidates by Ersilia.

## Identifiers

* EOS model ID: `eos7yti`
* Slug: `osm-series4`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Probability of killing P.falciparum in vitro (IC50 < 1uM and 2.5uM, respectively)

## References

* [Publication](https://pubs.acs.org/doi/10.1021/acscentsci.6b00086)
* [Source Code](https://github.com/ersilia-os/lazy-qsar)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos7yti)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7yti.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos7yti) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/10.1021/acscentsci.6b00086) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!