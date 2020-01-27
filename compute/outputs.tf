output "instance1nicid" {
  value = "${aws_instance.p1.primary_network_interface_id}"
}
output "instance2nicid" {
   value = "${aws_instance.p2.primary_network_interface_id}"
}
output "instance3nicid" {
   value = "${aws_instance.p3.primary_network_interface_id}"
}
output "instance4nicid" {
   value = "${aws_instance.p4.primary_network_interface_id}"
}