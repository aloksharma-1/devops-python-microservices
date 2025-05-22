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
├── task-service/
├── notifier-service/
├── kubernetes/
│   ├── auth-deployment.yaml
│   ├── task-deployment.yaml
│   └── notifier-deployment.yaml
├── terraform/
│   └── main.tf
├── cloudbuild.yaml
└── README.md
