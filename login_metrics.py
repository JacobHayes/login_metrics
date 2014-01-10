#!/usr/bin/env python3

def input_gen(file=False):
    if file == False:
        print("Use subprocess to get `lastb` data")
        #yield line
    else: #Depreciated, yes in 1.0 already
        with open(file) as f:
            for line in f:
                yield line
#input_gen

def most_occur(metric):
    return max(set(metric), key=metric.count)
#most_occur

def parse(line):

    sline = (line.split())

    y_value = None
    try:
        if sline[1][0:3] == "ssh":
            y_value = tuple(sline[0:3:2])
    except IndexError:
        pass
    finally:
        return y_value
#parse

t_reqs = list()
for line in input_gen("lastb_out"):
    pline = parse(line)
    if pline is not None:
        t_reqs.append(pline)
t_reqs_num = len(t_reqs)

# Requests
u_reqs = set(t_reqs)
u_reqs_num = len(u_reqs)
max_u_ip = most_occur(t_reqs)

print("Failed Login Requests")
print("  Total:  {t}".format(t = t_reqs_num))
print("  Unique: {u}".format(u = u_reqs_num))
print("  Percent unique: {p:.2f}%".format(p = 100*(u_reqs_num/t_reqs_num)))
print("  Highest occurring: {muip} at {muipc:.2f}%".format(muip = max_u_ip, muipc = 100*(t_reqs.count(max_u_ip)/len(t_reqs))))

print("")

# Usernames
u = [req[0] for req in t_reqs]
u_u = set(u)
max_u = most_occur(u)

print("  Usernames")
print("    Total:  {lun}".format(lun = len(u_u)))
print("    Highest occurring: {mun} at {munc:.2f}%".format(mun = max_u, munc = 100*(u.count(max_u)/len(u))))

print("")

# IP Addresses
ip = [req[1] for req in t_reqs]
u_ip = set(ip)
max_ip = most_occur(ip)

print("  IPs")
print("    Total: {lip}".format(lip = len(u_ip)))
print("    Highest occurring: {mip} at {mipc:.2f}%".format(mip = max_ip, mipc = 100*(ip.count(max_ip)/len(ip))))

print("")