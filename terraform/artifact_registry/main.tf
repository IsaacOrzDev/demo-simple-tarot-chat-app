variable "project_name" {
  type = string
}


terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = var.project_name
}

resource "google_artifact_registry_repository" "tarot_repo" {
  location      = "us-central1"
  repository_id = "tarot-repo"
  description   = "Tarot Repo"
  format        = "docker"
}

