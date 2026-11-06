Insurance Premium Prediction APIA production-ready machine learning web service built with FastAPI to predict medical insurance costs based on individual health parameters and demographics.Table of ContentsOverviewKey FeaturesTech StackProject ArchitectureInstallation & SetupDocker DeploymentAPI EndpointsUsage ExampleRepositoriesOverviewAccurate prediction of medical insurance costs helps insurance providers price policies effectively and allows customers to estimate their healthcare expenses. This project provides a containerized, high-performance API endpoint that accepts user demographic and health data to return real-time insurance cost estimates using a trained Machine Learning model.Key FeaturesFastAPI Backend: Asynchronous, high-performance web API framework with automatic OpenAPI documentation.Data Validation: Strict input data validation and serialization powered by Pydantic schemas.Machine Learning Integration: Pipeline integration for preprocessing data and generating real-time predictions.Dockerized: Packaged into a lightweight Docker container for consistent cross-environment deployment.RESTful Endpoints: Clean, well-structured endpoints for health checks and model inference.Tech StackLanguage: Python 3.10+API Framework: FastAPI, UvicornMachine Learning: Scikit-Learn, Pandas, NumPy, JoblibValidation: PydanticContainerization: DockerVersion Control & Registry: Git, GitHub, Docker HubProject Architectureinsurance-premium-prediction-fastapi/
│
├── artifacts/              # Trained models and scalers
│   └── model.pkl
├── notebook/               # Data analysis, feature engineering & training notebooks
├── src/                    # Source code directory
│   ├── pipeline/           # Prediction and training pipelines
│   ├── components/         # Data ingestion, transformation, model trainer
│   └── logger.py           # Logging module
│
├── app.py                  # FastAPI application entry point
├── Dockerfile              # Container configuration
├── requirements.txt        # Python package dependencies
├── setup.py                # Project packaging setup
└── README.md               # Project documentation
Installation & SetupPrerequisitesEnsure you have Python 3.9 or higher installed on your system.1. Clone the Repositorygit clone https://github.com/Pratham1603/insurance-premium-prediction-fastapi.git
cd insurance-premium-prediction-fastapi
2. Create and Activate a Virtual EnvironmentLinux / macOS:python3 -m venv venv
source venv/bin/activate
Windows:python -m venv venv
venv\Scripts\activate
3. Install Dependenciespip install -r requirements.txt
4. Run the ApplicationStart the FastAPI server using Uvicorn:uvicorn app:app --reload
The server will launch at http://127.0.0.1:8000.Docker DeploymentPull from Docker HubYou can pull and run the pre-built image directly from Docker Hub:docker pull pratham1603/insurance-premium-prediction-fastapi:latest
docker run -d -p 8000:8000 pratham1603/insurance-premium-prediction-fastapi:latest
Build Image LocallyTo build and run the Docker image from source:docker build -t insurance-premium-prediction-fastapi .
docker run -d -p 8000:8000 insurance-premium-prediction-fastapi
API EndpointsFastAPI automatically generates interactive documentation for testing endpoints:Swagger UI: http://127.0.0.1:8000/docsReDoc: http://127.0.0.1:8000/redocPrimary EndpointsMethodEndpointDescriptionGET/Root endpoint / System Status CheckPOST/predictPredicts insurance premium based on input featuresUsage ExamplePOST /predictRequest Body:{
  "age": 32,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "southeast"
}
cURL Request:curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 32,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "southeast"
}'
Response:{
  "predicted_premium": 5420.50
}
RepositoriesGitHub Repository: insurance-premium-prediction-fastapiDocker Hub Repository: pratham1603/insurance-premium-prediction-fastapi