In this workshop, the airflow deployment is given read-access to AWS Secrets
Manager by creating an IAM user through Terraform. The AWS environment
variables that allow Airflow to authenticate are passed in through Gitpod's
secrets. To do so,

1. Have keybase installed
2. Have a keybase profile (link with your DM colleagues as a bonus)
3. Run "terraform apply" and provide your keybase username when asked for it.
4. Decrypt the IAM SECRET ACCESS KEY and copy it and the AWS_ACCESS_KEY_ID to
   gitpod.io/variables, using the identifiers that are used in the .gitpod.yml
   file.
   Example:

   ```bash
   terraform output -raw pgp_encrypted_iam_secret_access_key \
     | base64 --decode \
     | keybase pgp decrypt
   ```

The solutions file, which is uploaded with the gitpod, is a base64 encoded 
tarball (compressed with gzip) of the solutions. Most people reading this, 
won't know how to get the files out, but you should now with that knowledge.

After exporting the env vars for AWS_*, one should `docker compose build` &
`docker compose up`.

For the capstone exercise, simply add a file with the prefix you mentioned to
the right S3 bucket. I'd recommend to do this once a few people have finished
that part and are running the sensor at a minutely frequency, so that they have
the feeling their sensor is acting as expected.
