<br/>
<p align="center">
    <img width="80%" src="./src/img/CWRU.jpg">
</p>
<br/>



<br/>

<h1 align="center">CSDS 458: Project</h1>
<h2 align="center">Redefining Cancer Treatment</h2>
<br/>

In this project..


## Instructions 

### Creating the Environment


> 🚧 Warning
> 
> The project was tested with a notebook having Windows 11 OS, 32GB RAM, Nvidia GTX 1660TI specs.


The `conda` environment is _strongly_ recommended. To create a `conda` environment for this project:

1. Open a terminal and navigate to the directory where project files are located.

2. Run the following command to create the environment:

    ```
    conda create python=3.8 --name CSDS458
    ```

    This will create a new `conda` environment named `CSDS458`.

3. Activate the environment by running the following command:

    ```
    conda activate CSDS458
    ```

4. Install the required packages by running the following command:

    ```
    conda install --file requirements.txt
    ```

    This will install all the packages listed in the `requirements.txt` file.

5. Though not strictly required, use the following command to be able to run the Jupyter notebooks.

    ```
    python -m ipykernel install --user --name PAWS --display-name "CSDS458"
    ```

6. Install Nvidia GPU Computing Toolkit CUDA v11.8. The installation of the requirements should take care of this step, but if does not work, be sure to install it from [here](https://developer.nvidia.com/cuda-11.0-download-archive).


## Training and Testing Phase

TODO


