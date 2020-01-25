# CSIRTG-PEERS

The FASTEST way to get the Spamhaus DBL information.

# Examples
## Shell
```bash
$ csirtg-spamhaus 71.6.146.130

{'description': 'Direct UBE sources, spam operations & spam services',
 'tags': 'spam'}

$ csirtg-spamhaus dbltest.com

{'description': 'spammed domain', 'tags': 'suspicious'}
```

## Python
```python
from csirtg_spamhaus import get
from pprint import pprint


pprint(get('71.6.146.130'))
```

# Before You Begin
If you're using 1.1.1.1 or 8.8.X.X you must set `NAMESERVERS` to a more 'local' nameserver (eg: your ISP).

```shell
$ export NAMESERVER=209.18.47.61
$ csirtg-spamhaus 71.6.146.130
```

This module takes advantage of the various Spamhaus XEN / DBL Lists. If you find this useful- support them!

https://www.spamhaus.org