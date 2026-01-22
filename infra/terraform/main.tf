# Basic Infrastructure Definition for Project OVERLORD
# Provider: AWS

provider "aws" {
  region = "us-east-1"
}

# 1. S3 Bucket for Master Assets
resource "aws_s3_bucket" "master_assets" {
  bucket = "overlord-master-assets-prod"
  tags = {
    Name        = "Project Overlord Assets"
    Environment = "Production"
  }
}

# 2. RDS PostgreSQL Instance
resource "aws_db_instance" "primary_db" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t3.micro" # Scale up for prod
  db_name              = "overlord_db"
  username             = var.db_username
  password             = var.db_password
  skip_final_snapshot  = true
  publicly_accessible  = false
}

# 3. SQS Queue for AI Processing Tasks
resource "aws_sqs_queue" "ai_processing_queue" {
  name                      = "ai-transformation-queue"
  delay_seconds             = 0
  message_retention_seconds = 86400 # 1 day
  receive_wait_time_seconds = 10
}

# 4. Redis (ElastiCache) for Task State
resource "aws_elasticache_cluster" "task_cache" {
  cluster_id           = "overlord-cache"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"
  port                 = 6379
}