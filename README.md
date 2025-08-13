# Fraud Transaction Detection

A modular and configurable machine learning pipeline to detect fraudulent transactions.  
This project follows a **component-based architecture** with clearly defined stages for **data ingestion**, **data validation**, **data transformation**, and **model training**.

---

## 📌 Features

- **Data Ingestion** – Reads and loads raw transaction data from specified sources.
- **Data Validation** – Validates schema, checks missing values, and ensures data integrity.
- **Data Transformation** – Preprocesses data, handles missing values, encodes categorical variables, and scales features.
- **Model Training** – Trains machine learning models on the processed data and generates evaluation metrics.
- **Logging & Exception Handling** – Integrated logging and custom exception handling for better debugging.

---

## 🛠 Project Structure

FraudTransactionDetection/
│
├── components/
│ ├── data_ingestion.py
│ ├── data_validation.py
│ ├── data_transformation.py
│ └── model_trainer.py
│
├── entity/
│ ├── config_entity.py
│
├── exception/
│ └── exception.py
│
├── logging/
│ └── logger.py
│
├── main.py # Entry point of the pipeline
└── requirements.txt


---

## 🚀 How It Works

The pipeline runs through the following steps in sequence:

1. **Data Ingestion**  
   Loads data from source into a working directory.  
   ```bash
    dataIngestion = DataIngestion(dataIngestionConfig)
    dataIngestionArtifact = dataIngestion.initiate_data_ingestion()
    ```
   
2. **Data Validation**  
   Ensures the data matches the expected schema and has no critical missing values.  
   ```bash
    dataValidation = DataValidation(dataIngestionArtifact, dataValidationConfig)
    dataValidationArtifact = dataValidation.initiate_data_validation()
    ```

3. **Data Transformation**  
   Converts raw data into model-ready format (feature scaling, encoding, etc.). 
   ```bash
    dataTransformation = DataTransformation(dataValidationArtifact, dataTransformationConfig)
    dataTransformationArtifact = dataTransformation.initiate_data_transformation()
    ```
   
4. **Model Training**  
   Trains and evaluates the machine learning model using transformed data. 
   ```bash
    modelTrainer = ModelTrainer(model_trainer_config, dataTransformationArtifact)
    modelTrainerArtifact = modelTrainer.initiate_model_trainer()
    ```
   
## ⚙️ Installation
1. Clone the repository
```bash

git clone https://github.com/Nivakaran-S/fraud-transaction-detection.git
cd fraud-transaction-detection

```

2. Create a virtual environment
```bash

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

```

3Install dependencies
```bash

pip install -r requirements.txt

```

## ▶️ Running the Pipeline
To run the full training pipeline:
```bash

python main.py

```

## 📝 Logging & Error Handling
- Logging: All logs are stored in the configured logging directory, making it easier to trace execution.
- Custom Exceptions: FraudTransactionException provides detailed error tracking.

## 📊 Example Outputs
Artifacts generated after pipeline execution:
- Data Ingestion Artifact – Paths to ingested train/test data.
- Data Validation Artifact – Validation status & report.
- Data Transformation Artifact – Paths to transformed datasets & preprocessing objects.
- Model Trainer Artifact – Trained model path & performance metrics.

## 🧩 Configuration
Configurations are defined in:
- config_entity.py – Holds configuration classes for all pipeline stages.
- TrainingPipelineConfig – Global pipeline configuration.

## 🤝 Contributing
Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.
