import re


def parseARP(arpTable):
    arp_list = []
    arpTable = arpTable.strip()
    for line in arpTable.splitlines():
      if re.search(r"^Address.*Interface$", line, flags=re.M):
        continue
      mac_address = line.split()[2]
      arp_list.append(mac_address)

    return arp_list


class FilterModule(object):
    def filters(self):
        return {"parseARP": parseARP }
