import dns.resolver
from dns.resolver import NoAnswer, NXDOMAIN, NoNameservers, Timeout
from dns.name import EmptyLabel

from csirtg_spamhaus.constants import TIMEOUT, NAMESERVER, RE_FQDN, RE_IPV4, \
    IP_CODES, FQDN_CODES


def _get(data, s, nameserver=NAMESERVER):
    data = '%s.%s.spamhaus.org' % (data, s)

    resolver = dns.resolver.Resolver()
    resolver.timeout = TIMEOUT
    resolver.lifetime = TIMEOUT
    if nameserver:
        resolver.nameservers = [nameserver]

    resolver.search = []

    try:
        answers = resolver.query(data, 'A')

    except (NoAnswer, NXDOMAIN, EmptyLabel, NoNameservers, Timeout) as e:
        e = str(e)
        if e.startswith('The DNS operation timed out after'):
            return

        if 'The DNS response does not contain' in e or \
                'None of DNS query names exist' in e:
            return

        raise

    if answers:
        return str(answers[0])


def get_dbl(data, nameserver=NAMESERVER):
    return _get(data, 'dbl', nameserver)


def get_zen(data, nameserver=NAMESERVER):
    data = '.'.join(reversed(data.split('.')))
    return _get(data, 'zen', nameserver)


def get(i, nameserver=NAMESERVER):
    if RE_IPV4.match(i):
        rv = get_zen(i, nameserver=nameserver)
        if rv:
            rv = IP_CODES.get(rv)

    elif RE_FQDN.match(i):
        rv = get_dbl(i, nameserver=nameserver)
        if rv:
            rv = FQDN_CODES.get(rv)

    else:
        raise ValueError('indicator not supported')

    return rv


def main():
    import sys
    from pprint import pprint

    # 'ns2.ndxylfpxuwowlhycfh.pw'
    # '71.6.146.130'

    i = sys.argv[1]

    pprint(get(i))


if __name__ == "__main__":
    main()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
