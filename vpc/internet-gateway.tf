resource "aws_internet_gateway" "gw" {
  vpc_id = "${aws_vpc.transit-gateway-vpc.id}"

  tags = {
    Name = "igw-transit-gateway-vpc"
  }
}
