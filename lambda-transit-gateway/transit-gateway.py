import boto3
import time
import sys

#create transit gateway
def create_transit_gateway():
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway(
        Description='string',
        Options={
            'AmazonSideAsn': 64512,
            'AutoAcceptSharedAttachments': 'disable',
            'DefaultRouteTableAssociation': 'enable',
            'DefaultRouteTablePropagation': 'enable',
            'VpnEcmpSupport': 'enable',
            'DnsSupport': 'enable',
            'MulticastSupport': 'enable'
        },
        DryRun=False
    )
    return response

#create transit gateway VPC attachment
def create_transit_gateway_vpc_attachment(transit_gateway_id, vpc_id, subnet_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_vpc_attachment(
        TransitGatewayId=transit_gateway_id,
        VpcId=vpc_id,
        SubnetIds=[
            subnet_id,
        ],
        Options={
            'DnsSupport': 'enable',
            'Ipv6Support': 'disable'
        },
        DryRun=False
    )
    return response

#Create transit gateway route-table
def create_transit_gateway_rt(transit_gateway_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_route_table(
        TransitGatewayId=transit_gateway_id,
        DryRun=False
    )
    return response

#Create transit gateway route
def create_transit_gateway_route(transit_gateway_rt_id, destination_ip_block, transit_gateway_attachment_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_route(
        DestinationCidrBlock=destination_ip_block,
        TransitGatewayRouteTableId=transit_gateway_rt_id,
        TransitGatewayAttachmentId=transit_gateway_attachment_id,
        Blackhole=False,
        DryRun=False
    )
    return response

#Create transit gateway multi-cast domain
def create_transit_gateway_multicast_domain(transit_gateway_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_multicast_domain(
        TransitGatewayId=transit_gateway_id,
        DryRun=False
    )
    return response

#Associate transit gateway multi cast domain
def associate_transit_gateway_multicast_domain(tgw_multicast_domain_id, tgw_attachment_id, subnetID):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.associate_transit_gateway_multicast_domain(
    TransitGatewayMulticastDomainId=tgw_multicast_domain_id,
    TransitGatewayAttachmentId=tgw_attachment_id,
    SubnetIds=[
        subnetID,
    ],
    DryRun=False
    )
    return response

#Delete transit gateway multi-cast domain
def delete_transit_gateway_multicast_domain(tgwy_multicast_domain_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.delete_transit_gateway_multicast_domain(
        TransitGatewayMulticastDomainId=tgwy_multicast_domain_id,
        DryRun=False
    )
    return response

#Delete transit gateway vpc attachment
def delete_transit_gateway_vpc_attachment(transit_gateway_attachment_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.delete_transit_gateway_vpc_attachment(
        TransitGatewayAttachmentId=transit_gateway_attachment_id,
        DryRun=False
    )
    return response

#Delete transit gateway
def delete_transit_gateway(transit_gateway_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.delete_transit_gateway(
        TransitGatewayId=transit_gateway_id,
        DryRun=False
    )

# dissacotiate transit gateway multicast domain
def disassociate_transit_gateway_multicast_domain(tgw_multicast_domain_id, tgw_attachment_id, subnet_id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.disassociate_transit_gateway_multicast_domain(
        TransitGatewayMulticastDomainId=tgw_multicast_domain_id,
        TransitGatewayAttachmentId=tgw_attachment_id,
        SubnetIds=[
            subnet_id,
        ],
        DryRun=False
    )
#register transit gateway multi-cast members
def register_transit_gateway_multicast_group_members(tgw_multicast_domain_id, group_address, network_interface2, network_interface3, network_interface4):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.register_transit_gateway_multicast_group_members(
    TransitGatewayMulticastDomainId = tgw_multicast_domain_id,
    GroupIpAddress = group_address,
    NetworkInterfaceIds = [
                              network_interface2, network_interface3, network_interface4
                          ],
    DryRun = False
    )
    return response

def register_transit_gateway_multicast_group_sources(tgw_multicast_domain_id, nic1id):
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.register_transit_gateway_multicast_group_sources(
        TransitGatewayMulticastDomainId=tgw_multicast_domain_id,
        GroupIpAddress='224.0.0.0',
        NetworkInterfaceIds=[
            nic1id,
        ],
        DryRun=False
    )
    return response


if __name__ == '__main__':
    action = sys.argv[1]

    if action == "apply":

        #Get variables from cmd line
        vpc_id = sys.argv[2]
        subnet_id = sys.argv[3]
        i1nic = sys.argv[4]
        i2nic = sys.argv[5]
        i3nic = sys.argv[6]
        i4nic = sys.argv[7]
        #Create transit gateway
        tgw_response = create_transit_gateway()
        #Collect transit gateway id from response
        tgw_id = tgw_response['TransitGateway']['TransitGatewayId']
        time.sleep(180)
        #Create transit gateway attachment
        tgw_attachment_response = create_transit_gateway_vpc_attachment(tgw_id, vpc_id, subnet_id)
        #get tgw attachment id response
        tgw_attachment_id = tgw_attachment_response['TransitGatewayVpcAttachment']['TransitGatewayAttachmentId']
        time.sleep(60)
        #Create transit gateway route table and get response
        tgw_rt_response = create_transit_gateway_rt(tgw_id)
        #Get transit gateway route table id from the response
        tgw_rt_id = tgw_rt_response ['TransitGatewayRouteTable']['TransitGatewayRouteTableId']
        time.sleep(90)
        #Create transit gateway route
        create_transit_gateway_route(tgw_rt_id, "10.123.111.0/24", tgw_attachment_id)
        #Create transit gateway multi cast domain
        tgw_multicast_domain_response = create_transit_gateway_multicast_domain(tgw_id)
        #Get transit gateway multi cast domain id
        tgw_multicast_domain_id = tgw_multicast_domain_response['TransitGatewayMulticastDomain']['TransitGatewayMulticastDomainId']
        time.sleep(90)
        #Associate transit gateway multi-cast domain
        associate_transit_gateway_multicast_domain(tgw_multicast_domain_id, tgw_attachment_id, subnet_id)
        time.sleep(30)
        #register transit gateway multicast group members
        register_transit_gateway_multicast_group_members(tgw_multicast_domain_id, "224.0.0.0", i2nic, i3nic, i4nic)
        time.sleep(30)
        #register transit gateway multicast group sources
        register_transit_gateway_multicast_group_sources(tgw_multicast_domain_id,i1nic)

    if action == "destroy":

        #Get values from input
        transit_gateway_multicast_domain_id = sys.argv[2]
        transit_gateway_attachment_id = sys.argv[3]
        transit_gateway_id = sys.argv[4]
        subnet_id = sys.argv[5]

        #Dissacotiate transit gate way multicast domain with subnet
        disassociate_transit_gateway_multicast_domain(transit_gateway_multicast_domain_id, transit_gateway_attachment_id, subnet_id)
        time.sleep(120)
        #Delete transit gateway multicast domain
        delete_transit_gateway_multicast_domain(transit_gateway_multicast_domain_id)
        time.sleep(120)
        #Delete transit gateway VPC attachment
        delete_transit_gateway_vpc_attachment(transit_gateway_attachment_id)
        time.sleep(120)
        #Delete transit gateway
        delete_transit_gateway(transit_gateway_id)




