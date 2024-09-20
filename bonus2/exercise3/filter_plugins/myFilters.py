import re


def arp_dict(arpTable):
#    print(arpTable)
#    print()

    arp_dict = {}
    arpTable = arpTable.strip()

#    print(arpTable.splitlines())
#    print()

    for line in arpTable.splitlines():
        if re.search(r".*Address.*Interface$", line, flags=re.M):
            continue
        ip_address = line.split()[1]
        mac_address = line.split()[3]
        arp_dict[ip_address] = mac_address

    return arp_dict

class FilterModule(object):
    def filters(self):
        return {"arp_dict": arp_dict}
