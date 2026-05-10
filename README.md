# End-To-End DL project with DVC

## Chicken Disease Classification

This project is an end-to-end Deep Learning pipeline built to classify chicken diseases (specifically Coccidiosis vs Healthy chickens) from fecal images. The project demonstrates the usage of **DVC (Data Version Control)** for tracking data, models, and building a reproducible pipeline.

## 🛠 Features

- **End-to-End Pipeline**: Includes Data Ingestion, Data Validation, Base Model Preparation, Training (with Callbacks), and Evaluation.
- **MLOps with DVC**: Pipeline tracking using `dvc.yaml`.
- **Modular Codebase**: Code is structured in an OOP format with clean separation of components, configuration, and pipelines.
- **Logging & Exception Handling**: Custom logging and exception tracking setup.
- **TensorFlow/Keras**: Uses Deep Learning models (like VGG16) to perform binary image classification.

---

## 🚀 Workflows

1. Update `config.yaml`
2. Update `secrets.yaml` (Optional)
3. Update `params.yaml`
4. Update the entity (in `src/chicken_disease_classification/entity/config_entity.py`)
5. Update the configuration manager (in `src/chicken_disease_classification/config/configuration.py`)
6. Update the components (in `src/chicken_disease_classification/components/`)
7. Update the pipeline (in `src/chicken_disease_classification/pipeline/`)
8. Update `main.py`
9. Update `dvc.yaml`

---

## ⚙️ How to Run?

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/Chicken-Disease-Classification.git
cd Chicken-Disease-Classification
```

### Step 2: Create a virtual environment and activate it

```bash
python -m venv env
# On Windows
env\Scripts\activate
# On Unix
source env/bin/activate
```

### Step 3: Install the requirements

```bash
pip install -r requirements.txt
```

### Step 4: Run the project through DVC

You can run the entire pipeline through DVC which ensures only the modified stages are re-run.

```bash
dvc repro
```

Alternatively, you can run `main.py` directly:

```bash
python main.py
```

---

## 📊 Evaluation & Metrics

The model evaluation scores (loss and accuracy) are captured in `scores.json` using DVC metrics:

```bash
dvc metrics show
```

## 🏗 Directory Structure

```text
├── artifacts/                  # Created during running the pipeline
├── config/
│   └── config.yaml             # Configurations for different pipeline stages
├── logs/                       # Application logs
├── src/                        # Main source code directory
│   └── chicken_disease_classification/
│       ├── components/         # Main business logic
│       ├── config/             # Configuration managers
│       ├── constants/          # Constant variables
│       ├── entity/             # Data classes
│       ├── exception.py        # Custom exception module
│       ├── logger.py           # Custom logging module
│       ├── pipeline/           # Scripts to run specific stages
│       └── utils/              # Helper functions
├── dvc.yaml                    # DVC pipeline file
├── main.py                     # Execution script
├── params.yaml                 # ML Model parameters (epochs, batch_size, learning rate...)
├── requirements.txt            # Python dependencies
└── setup.py                    # Setup script using setuptools
```
