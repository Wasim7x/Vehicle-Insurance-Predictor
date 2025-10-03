# 🚗 Vehicle Insurance Predictor

An end-to-end **Machine Learning project** that predicts whether a customer is likely to purchase a vehicle insurance policy. The project covers **data ingestion, preprocessing, validation, model training, evaluation, deployment**, and a **web interface** for real-time predictions.

---

## 📑 Table of Contents
- [✨ Features](#-features)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [▶️ Usage](#️-usage)
- [🧩 ML Workflow](#-ml-workflow)
- [🌐 Web Application](#-web-application)
- [🐳 Docker Support](#-docker-support)
- [📊 Experiments](#-experiments)
- [📜 Configuration](#-configuration)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## ✨ Features
- Automated **data ingestion** from multiple sources (CSV, databases).
- **Data validation** against schema definitions.
- **Data transformation** with preprocessing pipeline.
- **Model training** with ML algorithms.
- **Model evaluation** and metrics reporting.
- **Model storage** and retrieval with AWS S3.
- **Web app interface** using Flask/FastAPI for user predictions.
- **Dockerized** for consistent deployment.

---

## 📂 Project Structure
```
Vehicle-Insurance-Predictor/
│── app.py                 # Web application entry point
│── setup.py               # Setup script
│── pyproject.toml         # Project metadata & dependencies
│── requirements.txt       # Python dependencies
│── Dockerfile             # Docker image configuration
│── templates/             # HTML templates for web UI
│── static/css/            # Static assets (CSS)
│── config/                # Configuration files (schema, model)
│── src/                   # Source code
│   ├── components/        # Data ingestion, transformation, validation, training
│   ├── pipline/           # Training & prediction pipelines
│   ├── cloud_storage/     # AWS storage utilities
│   ├── configuration/     # Database & cloud configs
│   ├── entity/            # Entity & model definitions
│   ├── utils/             # Utility functions
│   ├── logger/            # Logging utility
│   ├── exception/         # Custom exceptions
│── artifact/              # Generated artifacts (datasets, models, reports)
│── notebook/              # Jupyter notebooks for experiments
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Wasim7x/Vehicle-Insurance-Predictor
cd Vehicle-Insurance-Predictor
```

### 2️⃣ Create a Virtual Environment
```bash
conda create -n venv python=3.10 -y
conda activate ./venv
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables
Create a `.env` file in the project root with your **AWS/MongoDB credentials**.

---

## ▶️ Usage

### Run Web Application
```bash
python app.py
```
Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Train Model
```bash
python src/pipline/training_pipeline.py
```

### Make Predictions
```bash
python src/pipline/prediction_pipeline.py
```

---

## 🧩 ML Workflow
1. **Data Ingestion** → Collects raw data and stores in `artifact/`.
2. **Data Validation** → Validates against `schema.yaml`.
3. **Data Transformation** → Applies preprocessing (`preprocessing.pkl`).
4. **Model Training** → Trains model and saves in `artifact/model_trainer/`.
5. **Model Evaluation** → Evaluates trained model.
6. **Model Pusher** → Pushes final model to S3/production.

---

## 🌐 Web Application
- Frontend: HTML + CSS (Flask/Jinja templates)
- Backend: Flask/FastAPI (`app.py`)
- Allows users to input vehicle/customer data and get predictions in real time.

---

## 🐳 Docker Support
### Build Image
```bash
docker build -t vehicle-insurance-predictor .
```

### Run Container
```bash
docker run -p 5000:5000 vehicle-insurance-predictor
```

---

## 📊 Experiments
- Prototyping & experiments in `notebook/experiments.ipynb`
- Dataset samples in `notebook/data.csv`
- Trained model checkpoints: `notebook/rf_model.pkl`

---

## 📜 Configuration
- **`config/model.yaml`** → ML model configurations.
- **`config/schema.yaml`** → Data validation schema.
- **AWS/MongoDB** credentials stored securely in `.env`.

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---


