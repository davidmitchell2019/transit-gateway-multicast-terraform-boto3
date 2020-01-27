resource "aws_route_table" "r" {
  vpc_id = "${aws_vpc.transit-gateway-vpc.id}"

  route {
    cidr_block = "0.0.0.0/24"
    gateway_id = "${aws_internet_gateway.gw.id}"
  }

  tags = {
    Name = "trnsit-gateway-rt"
  }
}