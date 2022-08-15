variable "region" {
  default     = "eu-west-1"
  description = "AWS region"
}

provider "aws" {
  region = var.region
  default_tags {
    tags = {
      createdby = "Oliver"
      /* createdon = formatdate("YYYY-MM-DD", timestamp()) */
      course    = "Getting things done with Apache Airflow"
    }
  }
}

