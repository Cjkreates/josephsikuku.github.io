# Terraform configuration for portfolio infrastructure
terraform {
  required_version = ">= 1.0"
  
  # Backend configuration (where state is stored)
  # In production, this would be cloud storage
  backend "local" {
    path = "terraform.tfstate"
  }
}

# Provider configuration
# This tells Terraform which cloud to use
# We're using "local" for learning, but this could be AWS, Azure, GCP
provider "local" {
  # Local provider doesn't need configuration
}

# Create local file infrastructure definition
resource "local_file" "portfolio_infrastructure" {
  filename = "infrastructure-output.txt"
  content = <<-EOT
  🏗️ PORTFOLIO INFRASTRUCTURE DEFINITION
  =====================================
  
  This file represents infrastructure that would be created in real cloud environments.
  
  Infrastructure Components Defined:
  - Web Server: Hosts portfolio website
  - Load Balancer: Distributes traffic
  - Database: Stores visitor analytics
  - CDN: Content delivery network
  - Monitoring: Performance tracking
  
  Cloud Resources (Simulated):
  - Compute: 2x virtual machines
  - Storage: 50GB disk space
  - Network: Virtual network with firewall
  - DNS: Custom domain routing
  
  This is defined as CODE using Terraform!
  
  To deploy for real, you would use:
  - AWS Provider: amazon web services
  - Azure Provider: microsoft azure  
  - GCP Provider: google cloud platform
  
  Next: Run 'terraform apply' to create this infrastructure!
  EOT
}

# Create infrastructure metadata
resource "local_file" "infrastructure_metadata" {
  filename = "infrastructure-metadata.json"
  content = jsonencode({
    environment = "production"
    terraform_version = "1.0+"
    resources_defined = [
      "web_server",
      "load_balancer", 
      "database",
      "cdn",
      "monitoring"
    ]
    cloud_providers_supported = [
      "aws",
      "azure",
      "gcp",
      "digitalocean"
    ]
    last_updated = timestamp()
  })
}

# Output values (what gets created)
output "infrastructure_summary" {
  value = <<-EOT
  🎉 Terraform Configuration Valid!
  
  Infrastructure Defined:
  - ${local_file.portfolio_infrastructure.filename}
  - ${local_file.infrastructure_metadata.filename}
  
  Next Steps:
  1. Run: terraform init
  2. Run: terraform plan  
  3. Run: terraform apply
  
  Your infrastructure is defined as CODE! 🏗️
  EOT
}

output "deployment_ready" {
  value = "✅ Terraform configuration ready for cloud deployment!"
}