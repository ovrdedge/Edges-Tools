__author__ = 'jedge'
##############################################################################
# The purpose of this script is to generate a spreadsheet of Cisco devices   #
# based on a seed ip address, username, and password. It has other settings  #
# also that will be required to login
##############################################################################

def is_ip_address(ip_string):
    ip_list = ip_string.split(".")
    if ip_list.len() != 4:
        return False
    int(ip_list[0])
    int(ip_list[1])
    int(ip_list[2])
    int(ip_list[3])
    if ip_list[0] > 0 and ip_list[0] < 224:
        octet1 = True
    if ip_list[1] >= 0 and ip_list[1] < 255:
        octet2 = True
    if ip_list[2] >= 0 and ip_list[2] < 255:
        octet3 = True
    if ip_list[3] >= 1 and ip_list[3] < 254:
        octet4 = True
    if octet1 and octet2 and octet3 and octet4:
        return True
    else:
        return False

def is_sane_string(string1):
    if string1.len() < 32:
        return True
    else:
        return False


# Main part of the Program
#-----------------------------------------------------------------------------

# Prompting for Seed Cisco Device, then validating input.
your_dumb = True
while your_dumb:
    seed_ipaddr = raw_input("Enter Seed Cisco Device: ")
    if is_ip_address(seed_ipaddr):
        your_dumb False

# Prompting for User name, then validating input.
your_dumb = True
while your_dumb:
    username = raw_input("Enter User Name: ")
    if is_sane_string(username):
        your_dumb False

# Prompting for Password, then validating input.
your_dumb = True
while your_dumb:
    password = raw_input("Enter Password: ")
    if is_sane_string(password):
        your_dumb False

