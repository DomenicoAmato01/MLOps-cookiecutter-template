# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Autore
{{ cookiecutter.author_name }}

## Setup del Progetto

1.  Crea e attiva l'ambiente Conda:
    ```bash
    conda env create -f environment.yml
    conda activate {{ cookiecutter.project_slug }}
    ```
2.  Configura il remote storage di DVC:
    ```bash
    dvc remote modify origin url {{ cookiecutter.dvc_remote_storage }}
    ```
3.  Esegui il pull dei dati (se presenti):
    ```bash
    dvc pull
    ```