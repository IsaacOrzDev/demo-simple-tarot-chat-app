variable "project_name" {
  type = string
}

variable "image" {
  type = string
}

variable "cohere_api_key" {
  type = string
}

variable "openai_api_key" {
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

resource "google_cloud_run_service" "default" {
  name     = "tarot-service"
  location = "us-central1"
  project  = var.project_name

  template {
    spec {
      containers {
        image = var.image
        env {
          name  = "COHERE_API_KEY"
          value = var.cohere_api_key
        }
        env {
          name  = "OPENAI_API_KEY"
          value = var.openai_api_key
        }
      }

    }
  }
}

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location = google_cloud_run_service.default.location
  project  = google_cloud_run_service.default.project
  service  = google_cloud_run_service.default.name

  policy_data = data.google_iam_policy.noauth.policy_data
}
