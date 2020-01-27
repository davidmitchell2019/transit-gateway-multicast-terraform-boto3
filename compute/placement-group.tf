resource "aws_placement_group" "multicast-reciever" {
  name     = "multicast-reciever-placement-group"
  strategy = "cluster"
}