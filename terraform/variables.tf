# Variables for our infrastructure
variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "portfolio-website"
}

variable "region" {
  description = "Cloud region for deployment"
  type        = string
  default     = "us-east-1"
}

variable "enable_monitoring" {
  description = "Enable infrastructure monitoring"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Tags for cloud resources"
  type        = map(string)
  default = {
    Project     = "Portfolio"
    Environment = "Production"
    ManagedBy   = "Terraform"
    Owner       = "DevOps"
  }
}