# 🚀 DevOps Python Microservices on Google Cloud

This is a **production-grade DevOps project** that demonstrates how to build, containerize, deploy, and manage **Python-based microservices** using **Docker**, **Kubernetes**, **Terraform**, and **CI/CD on Google Cloud Platform (GCP)**.

---

## 📌 Project Highlights

✅ 3 Flask Microservices (Auth, Task, Notifier)  
✅ Dockerized and Orchestrated with Kubernetes (GKE)  
✅ Infrastructure Provisioned via Terraform  
✅ CI/CD Using Google Cloud Build  
✅ Monitoring & Logging with Stackdriver  
✅ GitHub-Integrated Build Triggers  

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
Supports creating, reading, updating, and deleting tasks.  
**Port:** `5001`

### 🔔 Notifier Service
Sends task notifications (currently logs to console or simulates email).  
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
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/aloksharma-1/devops-python-microservices.git
cd devops-python-microservices
2️⃣ Run Microservices Locally (Optional)
bash
Copy
Edit
cd auth-service
pip install -r requirements.txt
python main.py
Repeat the above for task-service/ and notifier-service/.

3️⃣ Authenticate & Set Project in GCP
bash
Copy
Edit
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
4️⃣ Build & Push Docker Images
bash
Copy
Edit
docker build -t gcr.io/YOUR_PROJECT_ID/auth-service ./auth-service
docker push gcr.io/YOUR_PROJECT_ID/auth-service

docker build -t gcr.io/YOUR_PROJECT_ID/task-service ./task-service
docker push gcr.io/YOUR_PROJECT_ID/task-service

docker build -t gcr.io/YOUR_PROJECT_ID/notifier-service ./notifier-service
docker push gcr.io/YOUR_PROJECT_ID/notifier-service
5️⃣ Provision GKE Cluster with Terraform
bash
Copy
Edit
cd terraform
terraform init
terraform apply
6️⃣ Connect to the GKE Cluster
bash
Copy
Edit
gcloud container clusters get-credentials devops-cluster --region us-central1
7️⃣ Deploy Microservices to Kubernetes
bash
Copy
Edit
kubectl apply -f kubernetes/
8️⃣ Verify Kubernetes Resources
bash
Copy
Edit
kubectl get pods
kubectl get svc
🔎 Note the EXTERNAL-IP from the service list to access your APIs.

🔐 IAM Roles for Cloud Build Service Account
bash
Copy
Edit
PROJECT_ID="your-project-id"
SERVICE_ACCOUNT="$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')@cloudbuild.gserviceaccount.com"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT" \
  --role="roles/container.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT" \
  --role="roles/container.developer"
📊 Monitoring & Logging
Open Google Cloud Console:

Cloud Logging → Logs Explorer

Cloud Monitoring → GKE Dashboard

