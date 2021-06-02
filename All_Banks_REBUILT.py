from Bank_functions import random_abc_network, one_net, ordinal, \
    summarization, subnets, host_requirements, greater_16_networks
import ipaddress
import random

# Decimal to Binary conversion questions
file = open('dec_to_bin.txt', 'a')
for number in range(256):
    file.write(f'Type: F\n'
               f'{number+1}) Convert the decimal number {number} to an 8 bit binary number.\n'
               f'a. {number:08b}\n')
file.close()

# Decimal to Hex conversion questions
file = open('dec_to_hex.txt', 'a')
for number in range(256):
    file.write(f'Type: F\n'
               f'{number+1}) Convert the decimal number {number} to a hex number.\n'
               f'a. {number:02x}\nb. {number:02X}\n')
file.close()

# Binary to Decimal
file = open('bin_to_dec.txt', 'a')
for number in range(256):
    file.write(f'Type: F\n'
               f'{number+1}) Convert the 8 bit binary number {number:08b} to a decimal number.\n'
               f'a. {number}\n')
file.close()

# Binary to Decimal
file = open('bin_to_hex.txt', 'a')
for number in range(256):
    file.write(f'Type: F\n'
               f'{number+1}) Convert the 8 bit binary number {number:08b} to a hex number.\n'
               f'a. {number:02x}\n'
               f'b. {number:02X}\n')
file.close()

# hex to Decimal
file = open('hex_to_dec.txt', 'a')
for number in range(256):
    file.write(f'Type: F\n'
               f'{number+1}) Convert the hex number {number:02X} to a decimal number.\n'
               f'a. {number}\n')
file.close()

# hex to Binary
file = open('hex_to_bin.txt', 'a')
for number in range(256):
    file.write(f'Type: F\n'
               f'{number+1}) Convert the hex number {number:02X} to a 8 bit binary number.\n'
               f'a. {number:08b}\n')
file.close()

# Broadcast Address for a network
file = open('broadcast_questions.txt', 'a')
for number in range(1000):
    information = random_abc_network()
    network = information[1]
    broadcast = information[2]

    file.write(f'Type: F\n'
               f'{number+1}) What is the broadcast address for the {network} network\n'
               f'a. {broadcast}\n')
file.close()

# total hosts on a network question
file = open('total_hosts_questions.txt', 'a')
for number in range(1000):
    information = random_abc_network()
    network = information[1]

    file.write(f'Type: F\n'
               f'{number+1}) What is the maximum number of assignable hosts on the {network} network?\n'
               f'a. {network.num_addresses-2}\n')
file.close()

# questions about total number of hosts on a network
file = open('number_of_hosts_questions.txt', 'a')
for number in range(1000):
    information = greater_16_networks()
    network = information[0]
    number_of_hosts = random.randint(1, network.num_addresses * 2)

    if number_of_hosts <= network.num_addresses - 2:
        file.write(f'{number+1}) True or False. There are at least {number_of_hosts} assignable hosts on the {network} '
                   f'network?\n'
                   f'*a. True\n'
                   f'b. False\n')
    else:
        file.write(f'{number+1}) True or False. There are at least {number_of_hosts} assignable hosts on the {network} '
                   f'network?\n'
                   f'a. True\n'
                   f'*b. False\n')
file.close()

# longhand to short hand conversion; subnet to cdir
file = open('cdir_to_mask.txt', 'a')
for number in range(33):
    ip_address = '0.0.0.0'
    cidr_notation = f'/{number}'
    network = ipaddress.IPv4Network(ip_address + cidr_notation, False)
    subnet_mask = network.netmask

    file.write(f'Type: F\n'
               f'{number+1}) What is the shorthand corresponding to a subnet mask of {subnet_mask}?\n'
               f'a. {cidr_notation}\n')
file.close()

# is ip on a network/mask
file = open('is_ip_on_network.txt', 'a')
for number in range(1000):
    information = random_abc_network()
    ip_address = information[4]
    network = information[1]
    number_of_network_bits = information[5]
    max_number_of_network_bits = 30
    ip_on_net = network[random.randint(0, network.num_addresses - 2)]

    if number_of_network_bits + 1 > max_number_of_network_bits:
        new_network = ipaddress.IPv4Network(f'{ip_address}/{max_number_of_network_bits}', False)
    else:
        new_network = ipaddress.IPv4Network(f'{ip_address}/{number_of_network_bits + 1}', False)

    if ip_on_net in new_network:
        file.write(f'{number+1}) True or False. The {ip_on_net} address is on the {new_network} network.\n'
                   f'*a. True\n'
                   f'b. False\n')
    elif ip_on_net not in new_network:
        file.write(f'{number+1}) True or False. The {ip_on_net} address is on the {new_network} network.\n'
                   f'a. True\n'
                   f'*b. False\n')

file.close()

# last valid host on network
file = open('last_valid_host.txt', 'a')
for number in range(1000):
    information = random_abc_network()
    network = information[1]
    subnet_mask = information[3]

    file.write(f'Type: F\n'
               f'{number+1}) Enter the last valid host on the network {network[0]} {subnet_mask}.\n'
               f'a. {network[network.num_addresses - 2]}\n')
file.close()

# write the network id for this ip address
file = open('subnet_host_belongs_to.txt', 'a')
for number in range(1000):
    information = random_abc_network()
    network = information[1]
    subnet_mask = information[3]

    file.write(f'Type: F\n'
               f'{number+1}) Enter the subnet (network ID) the host '
               f'{network[random.randint(1, network.num_addresses - 2)]} {subnet_mask} belongs to.\n'
               f'a. {network[0]}\n')
file.close()

# hosts per subnet
file = open('number_of_hosts_per_subnet.txt', 'a')
for number in range(1000):
    information = greater_16_networks()
    network = information[0]
    cidr_notation = information[1]
    subnet_mask = network.netmask

    file.write(f'Type: F\n'
               f'{number+1}) What subnet mask would give {network.num_addresses - 2} hosts per subnet?\n'
               f'a. {cidr_notation}\n'
               f'b. {subnet_mask}\n')
file.close()

# network summarization
file = open('network_summarization.txt', 'a')
for number in range(1000):
    classes = [10, 172, 192]
    what_class = classes[random.randint(0, 2)]
    information1 = random_abc_network(what_class)
    information2 = random_abc_network(what_class)
    information3 = random_abc_network(what_class)
    network1 = information1[1]
    network2 = information2[1]
    network3 = information3[1]
    nets = [network1, network2, network3]

    file.write(f'Type: F\n'
               f'{number+1}) What is the smallest network that contains all of the following subnets: '
               f'{nets[0]} {nets[1]} {nets[2]}.\n'
               f'a. {one_net(nets)}\n')

file.close()

# vlsm questions base network = 10.0.0.0/12 with host requirements of 500k, 250k, 125K, 60k, 30k, 30k. Asks students for
# one of the subnets randomly (1 - 6). Should always expect the same single answer because all IPs in the base network
# are used.
original_network = '10.0.0.0/12'
file = open('vlsm_12.txt', 'a')
network_list = list(ipaddress.IPv4Network(original_network).supernet(new_prefix=8).subnets(new_prefix=12))
for number, network in enumerate(network_list):
    network_string = str(network)
    _host_requirements = host_requirements(network_string)
    networks = subnets(network_string, _host_requirements)
    subnet_answer_number = random.randint(0, 3)

    file.write(f'Type: F\n'
               f'{number+1}) Given the base network of {network} and the hosts requirements of {_host_requirements} '
               f'use vlsm and best practices to create the necessary subnets. What is the network and '
               f'CIDR (1.2.3.4/24) of the {ordinal(subnet_answer_number+1)} subnet you created\n'
               f'a. {networks[subnet_answer_number]}\n')
file.close()

# vlsm questions base network = 192.168.0.0/25 with host requirements of 50, 25, 10, 10. Asks students for one of the
# subnets randomly (1 - 4). Should always expect the same single answer because all IPs in the base network are used.
original_network = '192.168.0.0/25'
file = open('vlsm_25.txt', 'a')
network_list = list(ipaddress.IPv4Network(original_network).supernet(new_prefix=16).subnets(new_prefix=25))
for number, network in enumerate(network_list):
    network_string = str(network)
    _host_requirements = (50, 25, 10, 10)
    networks = subnets(network_string, _host_requirements)
    subnet_answer_number = random.randint(0, 3)

    file.write(f'Type: F\n'
               f'{number+1}) Given the base network of {network} and the hosts requirements of {_host_requirements} '
               f'use vlsm and best practices to create the necessary subnets. What is the network and '
               f'CIDR (1.2.3.4/24) of the {ordinal(subnet_answer_number + 1)} subnet you created\n'
               f'a. {networks[subnet_answer_number]}\n')
file.close()

# vlsm questions base network = 172.16.0.0/21 with host requirements of 1000, 500, 200, 100, 50, 35, 10, 10. Asks
# students for one of the subnets randomly (1 - 8). Should always expect the same single answer because all IPs in
# the base network are used.
original_network = '172.16.0.0/21'
file = open('vlsm_21.txt', 'a')
network_list = list(ipaddress.IPv4Network(original_network).supernet(new_prefix=12).subnets(new_prefix=21))
for number, network in enumerate(network_list):
    network_string = str(network)
    _host_requirements = (1000, 200, 50, 10)
    networks = subnets(network_string, _host_requirements)
    subnet_answer_number = random.randint(0, 3)
    
    file.write(f'Type: F\n'
               f'{number+1}) Given the base network of {network} and the hosts requirements of {_host_requirements} '
               f'use vlsm and best practices to create the necessary subnets. What is the network and '
               f'CIDR (1.2.3.4/24) of the {ordinal(subnet_answer_number + 1)} subnet you created\n'
               f'a. {networks[subnet_answer_number]}\n')
file.close()

# ABC network subnet summarization questions
file = open('abc_network_summarization.txt', 'a')
for number in range(1000):
    subnet_list = []
    information = summarization(random_abc_network())
    subnets = information[0]
    new_mask_number = information[1]
    parent_network = information[2]

    for x in subnets:
        subnet_list.append(x.with_prefixlen)

    file.write(f'Type: F\n'
               f'{number+1}) Enter the network that contains all of the following subnets: {subnet_list}.\n'
               f'a. {parent_network}\n')
file.close()
