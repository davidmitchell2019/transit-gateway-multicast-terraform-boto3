resource "aws_vpc" "transit-gateway-vpc" {
  cidr_block = "${var.subnet-mask}"
  enable_dns_support = "true"
  enable_dns_hostnames = "false"
  //instance_tenancy = "dedicated"
  tags = {
    Name = "transit-gateway-vpc"
  }
}