terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  # Note: In production, use a remote S3 backend for state
  # backend "s3" { ... }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project   = "OVERLORD"
      ManagedBy = "Terraform"
      Stage     = var.environment
    }
  }
}