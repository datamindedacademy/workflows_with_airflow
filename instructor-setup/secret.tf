resource "aws_secretsmanager_secret" "api_key" {
  name = "airflow/variables/weather-api-key"
  description = "API key for the OpenWeatherMap service"
}


resource "aws_secretsmanager_secret_version" "api_value" {
  secret_id     = aws_secretsmanager_secret.api_key.id
  secret_string = "some-key"
}
