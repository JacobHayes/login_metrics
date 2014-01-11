login_metrics
=============

Some basic login metrics for RHEL/Fedora boxes:

```
# Linux `lastb` parser to identify bad ssh login attempts. Collects
# the unique username and hostname/IP stats of failed logins.
```

Does not work on Debian/Ubuntu. See issue #1

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

####Sample Output

<pre>
SSH Failed Login Metrics
  - Attempts
      Total:  3111
      Unique: 760
      Percent unique: 24.43%

      Highest occurring: 'root@201.76.188.170' at 490 attempts
        % of uniques: 0.13%
        % of total:   15.75%
  - Users
      Total:  3111
      Unique: 751
      Percent unique: 24.14%

      Highest occurring: 'root' at 560 attempts
        % of uniques: 0.13%
        % of total:   18.00%
  - IPs
      Total:  3111
      Unique: 9
      Percent unique: 0.29%

      Highest occurring: '201.76.188.170' at 2990 attempts
        % of uniques: 11.11%
        % of total:   96.11%
</pre>

Future/ToDo
-----------

- Add ability show all IP/Users/Combos (or whatever other metrics are supported down the line)
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

- Strong function abstractions
- Shell execution + input (subprocess)
- Generators
- try/except/finally
