# devops-python-microservices
# 🚀 DevOps Python Microservices on Google Cloud

This is a production-grade DevOps project demonstrating how to build, containerize, deploy, and manage **Python-based microservices** using **Docker**, **Kubernetes**, **Terraform**, and **CI/CD on Google Cloud Platform**.

---

## 📌 Project Highlights

✅ 3 Microservices (Auth, Task, Notifier)  
✅ Dockerized and Orchestrated with Kubernetes (GKE)  
✅ Infrastructure Provisioned using Terraform  
✅ CI/CD using Google Cloud Build  
✅ Monitoring and Logs via Stackdriver  
✅ GitHub-integrated Cloud Build Trigger  

---

## 🛠️ Tech Stack

| Layer            | Tools Used                          |
|------------------|-------------------------------------|
| Language         | Python (Flask)                      |
| Containerization | Docker                              |
| Orchestration    | Kubernetes (GKE)                    |
| Infra as Code    | Terraform                           |
| CI/CD Pipeline   | Cloud Build + GitHub                |
| Image Registry   | Google Container Registry (GCR)     |
| Cloud Platform   | Google Cloud Platform (GCP)         |
| Monitoring       | Stackdriver / Cloud Monitoring      |

---

## 📁 Microservices Overview

### 🔐 Auth Service
Handles user registration and authentication.  
**Port:** `5000`

### ✅ Task Service
Create, read, update, and delete tasks.  
**Port:** `5001`

### 🔔 Notifier Service
Sends task notifications (console/email simulation).  
**Port:** `5002`

---

## 📦 Project Structure

```bash
.
├── auth-service/
│   ├── main.py
│   └── requirements.txt
├── task-service/
│   ├── main.py
│   └── requirements.txt
├── notifier-service/
│   ├── main.py
│   └── requirements.txt
├── kubernetes/
│   ├── auth-deployment.yaml
│   ├── task-deployment.yaml
│   └── notifier-deployment.yaml
├── terraform/
│   └── main.tf
├── cloudbuild.yaml
└── README.md

⚙️ Setup & Deployment Guide
1️⃣ Clone the Repo
git clone https://github.com/aloksharma-1/devops-python-microservices.git
cd devops-python-microservices

2️⃣ Run Microservices Locally (Optional)
cd auth-service
pip install -r requirements.txt
python main.py
Repeat for task-service/ and notifier-service/.

3️⃣ Authenticate and Set Project in GCP
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

4️⃣ Build & Push Docker Images
docker build -t gcr.io/YOUR_PROJECT_ID/auth-service ./auth-service
docker push gcr.io/YOUR_PROJECT_ID/auth-service

docker build -t gcr.io/YOUR_PROJECT_ID/task-service ./task-service
docker push gcr.io/YOUR_PROJECT_ID/task-service

docker build -t gcr.io/YOUR_PROJECT_ID/notifier-service ./notifier-service
docker push gcr.io/YOUR_PROJECT_ID/notifier-service

5️⃣ Provision GKE Cluster with Terraform
cd terraform
terraform init
terraform apply
6️⃣ Connect to GKE Cluster
gcloud container clusters get-credentials devops-cluster --region us-central1

7️⃣ Deploy Microservices to Kubernetes
kubectl apply -f kubernetes/

8️⃣ Verify Kubernetes Resources
kubectl get pods
kubectl get svc
# Note the EXTERNAL-IP to access services.

🔐 IAM Roles for Cloud Build Service Account
PROJECT_ID="your-project-id"
SERVICE_ACCOUNT="$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')@cloudbuild.gserviceaccount.com"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT" \
  --role="roles/container.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT" \
  --role="roles/container.developer"

📊 Monitoring & Logging
Use Google Cloud Console:
Cloud Logging → Logs Explorer

Cloud Monitoring → GKE Dashboard
