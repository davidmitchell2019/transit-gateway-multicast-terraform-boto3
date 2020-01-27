//allow ingress ssh and all egress traffic
resource "aws_security_group" "allow_tls" {
  name        = "allow-ssh-inbound"
  description = "allow-ssh-inbound"
  vpc_id      = "${aws_vpc.transit-gateway-vpc.id}"

  ingress {
    # TLS (change to whatever ports you need)
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    # Please restrict your ingress to only necessary IPs and ports.
    # Opening to 0.0.0.0/0 can lead to security vulnerabilities.
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}