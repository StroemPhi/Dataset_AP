# Dataset_AP

An attempt to create a metadata schema for datasets that is mapped to standard ontologies and application profiles, like schema.org and DCAT-AP.

## Website

[https://stroemphi.github.io/Dataset_AP](https://stroemphi.github.io/Dataset_AP)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [dataset_ap](src/dataset_ap)
    * [schema](src/dataset_ap/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/dataset_ap/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
