__author__ = 'jedge'
##############################################################################
# The purpose of this script is to generate a spreadsheet of Cisco devices   #
# based on a seed ip address, username, and password. It has other settings  #
# also that will be required to login
##############################################################################

import edgesTools
import os

# Main part of the Program
#-----------------------------------------------------------------------------

# Prompting for Seed Cisco Device, then validating input.
loop_again = True
while loop_again:
    seed_ipaddr = raw_input("Enter Seed Cisco Device: ")
    if edgesTools.is_ip_address(seed_ipaddr):
        loop_again False
    else:
        print "That doesn't look like a valid IP, please try again."

# Loading up the username / password variable.
print "Please tell me all the passwords you want to try. I'll let you know how"
print "many you've loaded starting with an index of '0'."
credential_count = 0
credentials=[]

loop_again = True
while loop_again:

    # Prompting for User name, then validating input.
    loop_again_inner = True
    while loop_again_inner:
        username = raw_input("Enter User Name: ")
        if edgesTools.is_sane_string(username):
            loop_again_inner False
        else:
            print "String to long, please try again."

    # Prompting for Password, then validating input.
    loop_again_inner = True
    while loop_again_inner:
        password = raw_input("Enter Password: ")
        if edgesTools.is_sane_string(password):
            loop_again_inner False
        else:
            print "String to long, please try again."

    credentials[credential_count] = {
        'username': username ,
        'password': password
    }

    credential_count += 1

# Prompting for output file, then validating input

#os.getcwd()