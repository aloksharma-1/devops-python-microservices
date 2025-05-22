provider "google" {
  project = "devops-project-460606"
  region  = "us-central1"
}

resource "google_container_cluster" "primary" {
  name               = "devops-cluster"
  location           = "us-central1"
  initial_node_count  = 1   # 2 se 1 kar diya

  node_config {
    machine_type = "e2-small"  # e2-medium se e2-small kar diya
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }
}
