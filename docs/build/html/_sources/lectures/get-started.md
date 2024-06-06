# Get Started

## Classical Python

### Basic Interpreter Installation (Latest)

To get started with Python, you'll need to install the Python interpreter. Follow these steps:

1. Visit the official [Python website](https://www.python.org/downloads/).
2. Download the latest version suitable for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the instructions. Ensure that you check the option to add Python to your system PATH.

### Package Manager

Python uses `pip` as its **package manager**, which is included with Python installations. 

You can install new packages using:

```bash
pip install package-name
```

To upgrade a package, use:

```bash
pip install --upgrade package-name
```

To list installed packages, use:

```bash
pip list
```

### Virtual Environment

Virtual environments are crucial for **managing dependencies** in different projects. 

To create a virtual environment:

1. Navigate to your project directory.

2. Run the following command:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

To deactivate, simply run `deactivate`.

## Conda

### Anaconda

Anaconda is a distribution of Python that includes many pre-installed packages and tools for data science and machine learning:

1. Download the installer from the [Anaconda website](https://www.anaconda.com/).
2. Run the installer and follow the instructions.
3. Launch Anaconda Navigator to manage environments and packages visually.

#### Practice
Basic operations with Anaconda management:

```bash
# Create a new environment
conda create -n [env-name] python=3.8
# Activate the environment
conda activate [env-name]
# Locate the environment
conda env list
# Install a package
conda install [package-name]
# List installed packages
conda list
# Deactivate the environment
conda deactivate
# Remove the environment
conda remove -n [env-name] --all
```
### Miniconda

Miniconda is a **lighter version** of Anaconda with just the essential packages. 

To install Miniconda:

1. Download the installer from the [Miniconda website](https://docs.anaconda.com/free/miniconda/miniconda-install/).
2. Follow the installation instructions.
3. Use the `conda` command to manage the package environment.

### Mamba

Mamba is a fast, robust, and cross-platform package manager for Conda. 

To install Mamba in your Conda environment:

```bash
conda install mamba -c conda-forge
```

You can then use Mamba similarly to Conda for managing packages:

```bash
mamba install package-name
```

### Example

> Use conda to create a customized environment for the project aiming at data analysis. 



## IDE

### PyCharm

PyCharm is a powerful IDE for Python development:

1. Download and install PyCharm from the [JetBrains website](https://www.jetbrains.com/pycharm/download/).
2. Open PyCharm and configure it for your Python interpreter.
3. Explore features like intelligent code completion, debugging, and version control integration.

### Visual Studio Code

Visual Studio Code (VS Code) is a lightweight, versatile editor with excellent Python support:

1. Download and install VS Code from the [official website](https://code.visualstudio.com/).
2. Install the Python extension from the Extensions marketplace.
3. Configure the Python interpreter and explore features like IntelliSense, debugging, and integrated terminal.

## Jupyter Notebook

### Installation

Jupyter Notebooks are interactive documents for code, text, and visualizations. To install Jupyter Notebook:

```bash
pip install notebook
```

Or, if you are using Conda:

```bash
conda install -c conda-forge notebook
```

### Interactive Interface

To start the Jupyter Notebook server, run:

```bash
jupyter notebook
```

This will open the Jupyter interface in your web browser, where you can create and manage notebooks.

### Hinterland

Hinterland provides code completion for Jupyter Notebooks. 
To install Hinterland:

```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

Enable Hinterland through the Jupyter Nbextensions tab in the notebook interface.

