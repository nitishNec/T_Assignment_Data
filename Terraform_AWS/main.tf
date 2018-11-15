provider "aws" {
  access_key = ""
  secret_key = ""
  region     = "us-east-1"
}

data "aws_availability_zones" "all" {}

### Creating EC2 instance
resource "aws_instance" "web" {
  ami                    = "${lookup(var.amis,var.region)}"
  count                  = "${var.count}"
  key_name               = "${var.key_name}"
  vpc_security_group_ids = ["${aws_security_group.instance.id}"]
  source_dest_check      = false
  instance_type          = "t2.micro"

  tags {
    Name = "${format("web-%03d", count.index + 1)}"
  }
}

### Creating Security Group for EC2
resource "aws_security_group" "instance" {
  name = "terraform-example-instance"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["23.48.231.86/32"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["23.48.231.86/32"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["23.48.231.86/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}

