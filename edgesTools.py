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
    if ip_list[1] >= 0 and ip_list[1] <= 255:
        octet2 = True
    if ip_list[2] >= 0 and ip_list[2] <= 255:
        octet3 = True
    if ip_list[3] >= 1 and ip_list[3] <= 254:
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
