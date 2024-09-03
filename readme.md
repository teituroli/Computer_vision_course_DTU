# Introduction to Deep Learning and Computer Vision at DTU 2024

## Prerequisites

Before getting started, ensure you have the following installed on your system. Note: only tested on windows: 

- **Anaconda**: You can download it [here](https://www.anaconda.com/download/success). It has only been tested using python 3.12. 
- **PyTorch**:  You can install it via Conda as shown below.

## Setting Up the Environment

To ensure all dependencies are installed and properly configured, follow these steps:

1. **Clone the repository**: 
    ```bash
    git clone https://github.com/teituroli/Computer_vision_course_DTU.git
    cd Computer_vision_course_DTU
    ```

2. **Create the Conda environment**: 
    This will create a new Conda environment using the `environment.yml` file provided in this repository. This file includes all the necessary packages and their versions.

    ```bash
    conda env create -f environment.yml
    ```

3. **Activate the environment**:
    After the environment is created, activate it using:

    ```bash
    conda activate .conda
    ```

4. **Verify PyTorch installation**:
    To ensure PyTorch is installed correctly, run the following command within the activated environment:

    ```python
    python -c "import torch; print(torch.__version__)"
    ```

    or run 
    ```python
    python test_if_coda_works.py
    ```

    This should output the version of PyTorch installed.
    
    If it doesent work, follow this guide from microsoft: [Link](https://learn.microsoft.com/en-us/windows/ai/windows-ml/tutorials/pytorch-installation)

## Updating the Environment

As the course progresses, there might be updates or additional packages required. To update the environment:

1. **Install new packages**:
    If new packages are needed, install them using Conda or pip while the environment is activated:

    ```bash
    conda install <package-name>
    ```
    or
    ```bash
    pip install <package-name>
    ```

2. **Update the environment.yml file**:
    After installing new packages, update the `environment.yml` file to capture these changes:

    ```bash
    conda env export --no-builds > environment.yml
    ```

3. **Share updates with others**:
    Commit and push the updated `environment.yml` file to the repository so that others can replicate the environment:

    ```bash
    git add environment.yml
    git commit -m "Updated environment with new packages"
    git push
    ```

3. **Also check if there are other updates**
    Check if another person has made updates:
    ```bash 
    git status 
    ```
    if another user has made changes, then it is preferable to pull their changes
    ```bash
    git pull
    ```

## Troubleshooting

- **Environment Issues**: If you encounter issues with the environment, you can try removing it and recreating it using the steps above:

    ```bash
    conda remove --name .conda --all
    conda env create -f environment.yml
    ```

- **PyTorch Compatibility**: If there are issues with PyTorch, ensure that your CUDA version (if using GPU) is compatible with the version of PyTorch you are installing. You can check compatibility [here](https://pytorch.org/get-started/previous-versions/).

## Contact

For any issues or questions regarding the course materials, please reach out to [Your Contact Information].

---

This repository is for educational purposes only, following the guidelines of DTU's 2024 curriculum.
