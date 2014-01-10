login_metrics
=============

Some basic login metrics for Linux boxes:

```
# Linux `lastb` parser to identify bad ssh login attempts. Collects
# the unique username and hostname/IP stats of failed logins.
```

Current
-------

- Read from `lastb` output (subprocess)
- Displays the following for Attempts, Users, and IPs:
  - Total
  - Unique
  - Percent unique
  - Highest occuring (with count)
    - Percent of uniques
    - Percent of total

Future
------

- Add command line input file to read from instead of `lastb` (Useful for (old) log files)

- Maybe make into a module for use in other monitoring software (of my own creation or other)

- Add docstrings to all functions and include information for doctests

- Compare info from `last` to `lastb` to see if any failed login attempts were later successful.
  - Send out email or something alerting a successful bad attempt.
  - Not particularly conclusive; valid user may fail a login if still using passwords

- Allow user to check for # of attempts from a specific IP or username.
  - Username will doubtlessly be mostly comprised of root user attempts.
  - Also enables metrics specific to a single object (IP or username):
    - Possibly allow a combine an IP and username

- Include time frame metrics
  - Might allow remedial DoS identification
    - Set connections/[smh] threshold
    - Upon reaching threshold, extra log and notify admin
    - Perhaps automatically add highest offending IP(s) to firewall block
  - Metric to select all failed connections between a period of time
    - From this data set, could also provide the specific metrics noted above

Python Features
---------------

- Shell execution + input (subprocess)
- Generators
- try/except/finally
- Strong function abstractions
