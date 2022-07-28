# IVA

## How to use
To run the experiment you will need PsychoPy.

### The easy way
*Works only on Windows*  
Just install [Standalone PsychPy](https://www.psychopy.org/download.html#download), then run iva.psyexp

### Anaconda and Miniconda
1. install [anaconda](https://docs.anaconda.com/anaconda/install/index.html) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) if you don't already have it. You can use [anaconda installers](https://www.anaconda.com/products/distribution#Downloads).
2. Create psychopy-env.yml containing:
    ```
    name: psychopy
    channels:
    - conda-forge
    dependencies:
    - python=3.8
    - psychopy
    - pip
    - pip:
    - psychtoolbox
    - pygame
    - pyo
    - pyparallel; platform_system != "Windows"
    - SoundFile; platform_system == "Windows"
    - websocket_client
    ```
3. If you are using linux make sure to install [webkitgtk](https://webkitgtk.org/).  
On Debian-based systems: `sudo apt install libwebkitgtk-1.0`  
On Arch-based systems: `yay -S webkitgtk`
4. Create a new environment using the yml file by running in anaconda Prompt: `conda env create -n psychopy -f psychopy-env.yml`
5. Activate the newly create environment by running: `conda activate psychopy`

Then, run the experiment in Python: `python iva.py`