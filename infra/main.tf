terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.60.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region  = "eu-west-1"
  profile = "PersonalAWSAccount"
}

# Create a VPC
resource "aws_vpc" "private_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_dynamodb_table" "data_table" {
  name             = "nfl-data"
  billing_mode     = "PROVISIONED"
  read_capacity    = 5
  write_capacity   = 5
  hash_key         = "id"
  stream_enabled   = true
  stream_view_type = "NEW_IMAGE"

  attribute {
    name = "id"
    type = "S"
  }

}

resource "aws_s3_bucket" "nfl-site" {
  bucket = "nfl-site-8acf57f2-f8f5-4a05-ab52-4674f2837beb"
}

resource "aws_s3_bucket_public_access_block" "nfl-site" {
  bucket = aws_s3_bucket.nfl-site.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "nfl-site" {
  bucket = aws_s3_bucket.nfl-site.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_ownership_controls" "ebab_website_ownership" {
  bucket = aws_s3_bucket.nfl-site.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_policy" "nfl-site" {
  bucket = aws_s3_bucket.nfl-site.id
  policy = data.aws_iam_policy_document.nfl-site.json
}


data "aws_iam_policy_document" "nfl-site" {
  statement {
    effect = "Allow"

    actions = ["s3:GetObject*"]

    resources = ["${aws_s3_bucket.nfl-site.arn}/*"]

    principals {
      type        = "Service"
      identifiers = ["cloudfront.amazonaws.com"]
    }

    condition {
      test = "StringEquals"
      values = [
        "arn:aws:cloudfront::${data.aws_caller_identity.chalice.account_id}:distribution/${aws_cloudfront_distribution.nfl-site.id}"
      ]
      variable = "aws:SourceArn"
    }
  }
  # statement {
  #   sid       = "HTTPSOnly"
  #   effect    = "Deny"
  #   actions   = ["s3:*"]
  #   resources = [aws_s3_bucket.nfl-site.arn, "${aws_s3_bucket.nfl-site.arn}/*"]
  #   principals {
  #     identifiers = ["*"]
  #     type        = "AWS"
  #   }
  #   condition {
  #     test     = "Bool"
  #     values   = [false]
  #     variable = "aws:SecureTransport"
  #   }
  # }
}

resource "aws_cloudfront_origin_access_control" "nfl-site" {
  name                              = "nfl-site"
  description                       = "Origin Access Control for the nfl-site CloudFront distribution"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

resource "aws_cloudfront_distribution" "nfl-site" {
  origin {
    domain_name              = aws_s3_bucket.nfl-site.bucket_regional_domain_name
    origin_access_control_id = aws_cloudfront_origin_access_control.nfl-site.id
    origin_id                = "NflSiteOrigin"
  }

  enabled             = true
  comment             = "nfl-site distribution"
  default_root_object = "current.html"
  aliases             = ["nfl.lgrv.net"]


  default_cache_behavior {
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "NflSiteOrigin"
    cache_policy_id        = "4135ea2d-6df8-44a3-9df3-4b5a84be39ad" # Caching disabled
    viewer_protocol_policy = "redirect-to-https"
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  restrictions {
    geo_restriction {
      locations        = []
      restriction_type = "none"
    }
  }

}
