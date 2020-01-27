module "vpc" {
  source = "./vpc"
  avaialabilty-zone = "${var.availability-zone}"
  subnet-mask = "${var.subnet-mask}"
}
module "compute" {
  source = "./compute"
  availability-zone = "us-east-1a"
  subnet-id = "${module.vpc.subnet-id}"
}