# NFL Fun Index - Serverless

A website that scrapes data from sources and rates past NFL games on how fun they were to watch.

This was previously a Flask app deployed on a VPS with Docker and Nginx, but I have recently rewritten it to use serverless microservices on AWS, all defined as infrastructure-as-code, with automated, reproducible builds.

### Built with

- Python 3.9
- AWS Chalice & boto3
- Lambda for compute
- DynamoDB for persistence
- S3 for static web page storage and hosting
- BeautifulSoup and Selenium for scraping
- Pandas for tabular data handling
- Jinja2 for website templates

### Installation

#### Prerequisites:
- Python 3.9
- Terraform
- Poetry, the Python package manager
- An AWS account
- GNU Make

#### Process:
* Clone this repository
* `cd` into the root directory
* Run `make deploy` to run the build and deploy process

### License

This project is licensed under the MIT License - see the LICENSE.md file for details
