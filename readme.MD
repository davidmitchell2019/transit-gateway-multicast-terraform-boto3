Creates a transit gateway multi-cast domain in N Virginia US_EAST-1

PLEASE RUN THESE COMMANDS TO BUILD

aws configure
Set access key, secret key and region to us-east-1
Terraform init
Terraform apply -auto-approve
VPC_ID=$(terraform output vpc-id)
SUBNET_ID=$(terraform output subnet-id)
INSTANCE1_NIC_ID=$(terraform output instance1nicid)
INSTANCE2_NIC_ID=$(terraform output instance2nicid)
INSTANCE3_NIC_ID=$(terraform output instance3nicid)
INSTANCE4_NIC_ID=$(terraform output instance4nicid)

python lambda-transit-gateway/transit-gateway.py apply $VPC_ID $SUBNET_ID $INSTANCE1_NIC_ID $INSTANCE2_NIC_ID $INSTANCE3_NIC_ID $INSTANCE4_NIC_ID



PLEASE RUN THESE COMMANDS TO Destroy

please substitute values for 

-transit-gateway_multicast_domain_id 
-transit_gateway_attachment_id 
-transit_gateway_id 
-subnet_id

You will need to get these from the portal

for example:

python lambda-transit-gateway/transit-gateway.py destroy tgw-mcast-domain-076e83ed41fcf4074 tgw-attach-09eb748463cdc3c91 tgw-07b5d95bd783cf5d8 subnet-0019c7d51c9a8d86d

terraform destroy -auto-approve transit-gateway_multicast_domain_id transit_gateway_attachment_id transit_gateway_id subnet_id
