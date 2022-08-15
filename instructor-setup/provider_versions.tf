terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.38.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "3.3.0"
    }

    local = {
      source  = "hashicorp/local"
      version = "2.2.3"
    }

    null = {
      source  = "hashicorp/null"
      version = "3.1.1"
    }
  }

  required_version = ">= 0.14"
}

