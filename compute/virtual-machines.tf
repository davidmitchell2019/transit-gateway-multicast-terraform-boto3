
#Processor instance
resource "aws_instance" "p1" {
  //Use dummy ami for testing
  ami           = "ami-062f7200baf2fa504"
  //ami-02afd4e3e05c50a02
  instance_type = "c5.2xlarge"
  placement_group = "${aws_placement_group.multicast-reciever.id}"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"

  tags = {
    Name = "processor-1"
  }
}
#Processor instance
resource "aws_instance" "p2" {
  //use dummy ami for testing
  ami           = "ami-062f7200baf2fa504"
  //ami-02afd4e3e05c50a02
  instance_type = "c5.2xlarge"
  placement_group = "${aws_placement_group.multicast-reciever.id}"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"

  tags = {
    Name = "processor-2"
  }
}
#Processor instance
resource "aws_instance" "p3" {
  //use dummy ami for testing
  ami           = "ami-062f7200baf2fa504"
  //ami-02afd4e3e05c50a02
  instance_type = "c5.2xlarge"
  placement_group = "${aws_placement_group.multicast-reciever.id}"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"

  tags = {
    Name = "processor-3"
  }
}
#Processor instance
resource "aws_instance" "p4" {
  //use dummy ami for testing
  ami           = "ami-062f7200baf2fa504"
  //ami-02afd4e3e05c50a02
  instance_type = "c5.2xlarge"
  placement_group = "${aws_placement_group.multicast-reciever.id}"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"

  tags = {
    Name = "processor-4"
  }
}
#Config instance
resource "aws_instance" "c1" {
  //use dummy ami for testing
  ami           = "ami-062f7200baf2fa504"
  //ami-08368a7d06b4626f4
  instance_type = "t2.small"
  availability_zone = "${var.availability-zone}"
  subnet_id = "${var.subnet-id}"
  source_dest_check = "false"

  tags = {
    Name = "config-instance"
  }
}

