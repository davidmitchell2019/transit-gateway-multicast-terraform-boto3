output "vpc-id" {
  value = "${module.vpc.vpc-id}"
}
output "subnet-id" {
  value = "${module.vpc.subnet-id}"
}
output "instance1nicid" {
  value = "${module.compute.instance1nicid}"
}
output "instance2nicid" {
   value = "${module.compute.instance2nicid}"
}
output "instance3nicid" {
   value = "${module.compute.instance3nicid}"
}
output "instance4nicid" {
   value = "${module.compute.instance4nicid}"
}