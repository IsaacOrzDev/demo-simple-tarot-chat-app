cd ./terraform/cloud_run
terraform init
terraform apply -var-file="../variables.tfvars"
