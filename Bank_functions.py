import ipaddress
import random


# seems to work finding the smallest subnet that also contains all the networks given.
def one_net(_subnets):
    """
    Get the one IP network that covers all subnets in input or None is subnets are disjoint.
    """
    if len(_subnets) == 0:
        return None

    minimum_length = min([net.prefixlen for net in _subnets])
    while _subnets.count(_subnets[0]) < len(_subnets) and minimum_length > 0:
        # all subnets are not (yet) equal
        _subnets = [net.supernet(new_prefix=minimum_length) for net in _subnets]
        minimum_length -= 1

    # 0.0.0.0/? -> no common subnet
    if _subnets[0].network_address == ipaddress.ip_address(u'0.0.0.0'):
        return None

    return _subnets[0]


# function to generate a random A, B, or C ip address. unless 10, 172, or 192 is passed then first octet is set to that
# and that class ip is generated. Remember that Info is returned in a tuple and must be set to a variable/list to be
# called.
def random_abc_network(class_octet=-1):
    # determine class A, B, or C
    classes = [10, 172, 192]
    ip_address = ''
    number_of_network_bits = 0

    if class_octet not in classes:
        first_octet = classes[random.randint(0, 2)]
    else:
        first_octet = class_octet
    # Actually do some work (make ip and other info)
    if first_octet == 10:
        ip_address = f'10.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
        number_of_network_bits = random.randint(8, 30)
    elif first_octet == 172:
        ip_address = f'172.{random.randint(16, 31)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
        number_of_network_bits = random.randint(12, 30)
    elif first_octet == 192:
        ip_address = f'192.168.{random.randint(1, 255)}.{random.randint(1, 255)}'
        number_of_network_bits = random.randint(16, 30)

    cidr_notation = f'/{number_of_network_bits}'
    network_id = ipaddress.IPv4Network(ip_address + cidr_notation, False)
    broadcast = network_id.broadcast_address
    subnet_mask = network_id.netmask

    return cidr_notation, network_id, broadcast, subnet_mask, ip_address, number_of_network_bits


# network_info = random_abc_network(192)
# print(f'CIDR notation: {network_info[0]}')
# print(f'Network ID: {network_info[1]}')
# print(f'Broadcast: {network_info[2]}')
# print(f'Subnet Mask: {network_info[3]}')
# print(f'IP Address: {network_info[4]}')
# print(f'Number of network bits: {network_info[5]}')


def ordinal(num):
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    # I'm checking for 10-20 because those are the digits that don't follow the normal counting scheme.
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = suffixes.get(num % 10, 'th')
    return str(num) + suffix


# for i in range(1, 100):
#     print(ordinal(i))

def summarization(function):
    information = function
    parent_network = information[1]
    number_of_network_bits = information[5]

    if number_of_network_bits <= 27:
        new_mask_number = number_of_network_bits + random.randint(1, 3)
    elif number_of_network_bits == 28:
        new_mask_number = number_of_network_bits + random.randint(1, 2)
    elif number_of_network_bits == 29:
        new_mask_number = number_of_network_bits + 1
    else:
        new_mask_number = 30

    _subnets = parent_network.subnets(new_prefix=new_mask_number)

    return _subnets, new_mask_number, parent_network


def host_requirements(network):
    starting_mask_number = int(network[-2:]) + 1
    starting_max_hosts = 2 ** (32 - starting_mask_number) - 2
    network1 = random.randint(2, starting_max_hosts)
    network2 = random.randint(2, network1//2)
    network3 = random.randint(2, network2//2)
    network4 = random.randint(2, network3)

    return network1, network2, network3, network4


def subnets(parent_network, _host_requirements):
    network = ipaddress.IPv4Network(parent_network)
    subnet_list = [0, 1, 2, 3]

    for i in range(4):
        if _host_requirements[i] == 2:
            subnet_list[i] = list(network.subnets(new_prefix=30))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=30))[1]
        elif _host_requirements[i] <= 6:
            subnet_list[i] = list(network.subnets(new_prefix=29))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=29))[1]
        elif _host_requirements[i] <= 14:
            subnet_list[i] = list(network.subnets(new_prefix=28))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=28))[1]
        elif _host_requirements[i] <= 30:
            subnet_list[i] = list(network.subnets(new_prefix=27))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=27))[1]
        elif _host_requirements[i] <= 62:
            subnet_list[i] = list(network.subnets(new_prefix=26))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=26))[1]
        elif _host_requirements[i] <= 126:
            subnet_list[i] = list(network.subnets(new_prefix=25))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=25))[1]
        elif _host_requirements[i] <= 254:
            subnet_list[i] = list(network.subnets(new_prefix=24))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=24))[1]
        elif _host_requirements[i] <= 510:
            subnet_list[i] = list(network.subnets(new_prefix=23))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=23))[1]
        elif _host_requirements[i] <= 1022:
            subnet_list[i] = list(network.subnets(new_prefix=22))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=22))[1]
        elif _host_requirements[i] <= 2046:
            subnet_list[i] = list(network.subnets(new_prefix=21))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=21))[1]
        elif _host_requirements[i] <= 4094:
            subnet_list[i] = list(network.subnets(new_prefix=20))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=20))[1]
        elif _host_requirements[i] <= 8190:
            subnet_list[i] = list(network.subnets(new_prefix=19))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=19))[1]
        elif _host_requirements[i] <= 16382:
            subnet_list[i] = list(network.subnets(new_prefix=18))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=18))[1]
        elif _host_requirements[i] <= 32766:
            subnet_list[i] = list(network.subnets(new_prefix=17))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=17))[1]
        elif _host_requirements[i] <= 65534:
            subnet_list[i] = list(network.subnets(new_prefix=16))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=16))[1]
        elif _host_requirements[i] <= 131070:
            subnet_list[i] = list(network.subnets(new_prefix=15))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=15))[1]
        elif _host_requirements[i] <= 262142:
            subnet_list[i] = list(network.subnets(new_prefix=14))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=14))[1]
        elif _host_requirements[i] <= 524286:
            subnet_list[i] = list(network.subnets(new_prefix=13))[0]
            if i < 3:
                subnet_list[i + 1] = list(network.subnets(new_prefix=13))[1]

        if i < 3:
            network = subnet_list[i + 1]

    return subnet_list


def greater_16_networks():
    classes = [172, 192]
    first_octet = classes[random.randint(0, 1)]

    if first_octet == 172:
        ip_address = f'172.{random.randint(16, 31)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
        number_of_network_bits = random.randint(16, 30)
    else:
        ip_address = f'192.168.{random.randint(1, 255)}.{random.randint(1, 255)}'
        number_of_network_bits = random.randint(24, 30)

    cidr_notation = f'/{number_of_network_bits}'
    network = ipaddress.IPv4Network(ip_address + cidr_notation, False)

    return network, cidr_notation
