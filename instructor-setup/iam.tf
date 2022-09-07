variable "keybase_user" {
  description = <<-EOM
    Enter the keybase id of a person to encrypt the AWS IAM secret access key.
    Note that you need access to its private key so you can decrypt it. In
    practice that means you specify your own keybase account id.
    EOM
}

resource "aws_iam_user" "airflow" {
  name = "airflow"
  path = "/system/"
}

resource "aws_iam_access_key" "airflow" {
  user    = aws_iam_user.airflow.name
  pgp_key = "keybase:${var.keybase_user}"
}

resource "aws_iam_user_policy" "airflow_permissions" {
  name = "read_all_secrets"
  user = aws_iam_user.airflow.name

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetResourcePolicy",
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret",
                "secretsmanager:ListSecretVersionIds",
                "secretsmanager:ListSecrets"
            ],
            "Resource": ["*"]
        },
        {
            "Effect": "Allow",
            "Action": [
              "s3:GetObject"
            ],
            "Resource": ["arn:aws:s3:::dmacademy-course-assets/airflow/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
              "s3:ListBucket"
            ],
            "Resource": ["arn:aws:s3:::dmacademy-course-assets"]
        }

    ]
}
EOF
}

output "iam_access_key" {
    value = aws_iam_access_key.airflow.id
}

output "pgp_encrypted_iam_secret_access_key" {
  value = aws_iam_access_key.airflow.encrypted_secret
# Decrypt using your private PGP key:
# terraform output -raw iam_access_key | base64 --decode | keybase pgp decrypt
}
