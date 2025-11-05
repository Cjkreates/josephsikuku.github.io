# Output definitions - what Terraform shows after applying
output "portfolio_url" {
  description = "URL where portfolio is deployed"
  value       = "https://${var.app_name}.${var.region}.apps.example.com"
}

output "infrastructure_details" {
  description = "Details of created infrastructure"
  value = {
    environment    = var.environment
    app_name       = var.app_name
    region         = var.region
    monitoring     = var.enable_monitoring
    managed_by     = "Terraform"
  }
}

output "next_steps" {
  description = "Next steps for deployment"
  value = <<-EOT
  🚀 Infrastructure Definition Complete!
  
  To deploy to real cloud:
  1. Set up cloud provider credentials
  2. Update provider configuration
  3. Run: terraform init
  4. Run: terraform plan
  5. Run: terraform apply
  
  Your cloud infrastructure will be created automatically! ☁️
  EOT
}