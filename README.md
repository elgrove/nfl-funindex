# NFL Fun Index - Serverless

A website that scrapes data from sources and rates past NFL games on how fun they were to watch.

This was previously a Flask app deployed on a VPS with Docker and Nginx, but I have recently rewritten it to use serverless microservices on AWS, all defined as infrastructure-as-code, with automated, reproducible builds.

### How it works

- Running `make deploy` triggers the build and deploy process
- AWS Lambda functions are written in Python using the AWS Chalice framework, with a simple FastAPI-like decorator interface
- Chalice has a little-known function that can emit Terraform `.tf.json` files defining the Lambdas as AWS resources and all the accompanying policies, roles, CloudWatch events, etc
- This Terraform json is combined with typical Terraform HCL configuring additional resources that Chalice isn't able to, like DynamoDB and S3

### Installation

#### Prerequisites:
- Python 3.9
- Terraform
- Poetry, the Python package manager
- An AWS account configured in your ~/.aws directory
- GNU Make

#### Process:
* Clone this repository
* `cd` into the root directory
* Run `make deploy` to run the build and deploy process

### Built with

- Python 3.9
- AWS Chalice & boto3
- Lambda for compute
- DynamoDB for persistence
- S3 for static web page storage and hosting
- BeautifulSoup and Selenium for scraping
- Pandas for tabular data handling
- Jinja2 for website templates


### License

This project is licensed under the MIT License - see the LICENSE.md file for details
