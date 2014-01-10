#!/usr/bin/env python3

import subprocess

def get_metric_params(parent):
    metric = set(parent[0])
    metric_num = len(metric)
    percent_metric = 100*(metric_num/parent[1])
    highest, highest_metric_num, highest_parent_num = highest_occur(parent[0], metric)
    percent_metric_highest = 100*(highest_metric_num/metric_num)
    percent_total_highest  = 100*(highest_parent_num/parent[1])

    return(metric, metric_num, percent_metric, highest, highest_parent_num, percent_metric_highest, percent_total_highest)
#get_metric_params

def highest_occur(parent, metric):
    highest = max(set(parent), key=parent.count)
    metric_count = tuple(metric).count(highest)
    parent_count = parent.count(highest)
    return(highest, metric_count, parent_count)
#highest_occur

def lastb_gen():
    lastb_out = subprocess.Popen("lastb", stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split("\n")

    for line in lastb_out:
        yield parse(line)
#lastb_gen

def parse(line):
    sline = (line.split())

    y_value = None
    try:
        if sline[1][0:3] == "ssh":
            y_value = tuple(sline[0:3:2])
    except IndexError:
        pass
    finally:
        return(y_value)
#parse

def print_metric(metric, parent_total, metric_info):
    attempt = metric_info[3] if type(metric_info[3]) != tuple else metric_info[3][0] + "@" + metric_info[3][1]

    print("  - {}".format(metric))
    print("      Total:  {}".format(parent_total))
    print("      Unique: {}".format(metric_info[1]))
    print("      Percent unique: {:.2f}%".format(metric_info[2]))
    print("")
    print("      Highest occurring: {} at {} attempts".format(attempt, metric_info[4]))
    print("        % of uniques: {:.2f}%".format(metric_info[5]))
    print("        % of total:   {:.2f}%".format(metric_info[6]))
#print_metric

# Build master parent list; all failed login attempts
tmp_atmpts = list()
for line in lastb_gen():
    if line is not None:
        tmp_atmpts.append(line)
atmpts = (tmp_atmpts, len(tmp_atmpts))

if atmpts[1] > 0:
    print("SSH Failed Login Metrics")

    # Create user parent list; all users (dups)
    tmp_users = tuple(atmpt[0] for atmpt in atmpts[0])
    users = (tmp_users, len(tmp_users))

    # Create IP parent list; all IPs (dups) 
    tmp_ips = tuple(atmpt[1] for atmpt in atmpts[0])
    ips = (tmp_ips, len(tmp_ips))

    # Attempts
    # u_atmpts = get_metric_params(atmpts)
      # May want this later b/c it contains the actual unique data
    print_metric("Attempts", atmpts[1], get_metric_params(atmpts))
    
    # Users
    # u_users = get_metric_params(users)
      # May want this later b/c it contains the actual unique data
    print_metric("Users", users[1], get_metric_params(users))
    
    # IPs
    # u_ips = get_metric_params(ips)
      # May want this later b/c it contains the actual unique data
    print_metric("IPs", ips[1], get_metric_params(ips))
else:
    print("No failed logins")