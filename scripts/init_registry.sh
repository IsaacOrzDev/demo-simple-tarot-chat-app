cd ./terraform/artifact_registry
terraform init
terraform apply -var-file="../variables.tfvars"
