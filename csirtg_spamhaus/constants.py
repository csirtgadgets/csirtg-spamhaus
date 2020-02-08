import os
import re

TIMEOUT = 5

NAMESERVER = os.getenv('NAMESERVER')


RE_IPV4 = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(\d{1,3})$')
RE_FQDN = re.compile(r'^((?!-))(xn--)?[a-z0-9][a-z0-9-_\.]{0,245}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$')


FQDN_CODES = {
    '127.0.1.2': {
        'tags': 'suspicious',
        'description': 'spammed domain',
    },
    '127.0.1.3': {
        'tags': 'suspicious',
        'description': 'spammed redirector / url shortener',
    },
    '127.0.1.4': {
        'tags': 'phishing',
        'description': 'phishing domain',
    },
    '127.0.1.5': {
        'tags': 'malware',
        'description': 'malware domain',
    },
    '127.0.1.6': {
        'tags': 'botnet',
        'description': 'Botnet C&C domain',
    },
    '127.0.1.102': {
        'tags': 'suspicious',
        'description': 'abused legit spam',
    },
    '127.0.1.103': {
        'tags': 'suspicious',
        'description': 'abused legit spammed redirector',
    },
    '127.0.1.104': {
        'tags': 'phishing',
        'description': 'abused legit phish',
    },
    '127.0.1.105': {
        'tags': 'malware',
        'description': 'abused legit malware',
    },
    '127.0.1.106': {
        'tags': 'botnet',
        'description': 'abused legit botnet',
    },
    '127.0.1.255': {
        'description': 'BANNED',
    },
}


IP_CODES = {
    '127.0.0.2': {
        'tags': 'spam',
        'description': 'Direct UBE sources, spam operations & spam services',
    },
    '127.0.0.3': {
        'tags': 'spam',
        'description': 'Direct snowshoe spam sources detected via automation',
    },
    '127.0.0.4': {
        'tags': ['exploit', 'malware'],
        'description': 'CBL + customised NJABL. 3rd party exploits (proxies, '
                       'trojans, etc.)',
    },
    '127.0.0.5': {
        'tags': ['exploit', 'malware'],
        'description': 'CBL + customised NJABL. 3rd party exploits (proxies, '
                       'trojans, etc.)',
    },
    '127.0.0.6': {
        'tags': ['exploit', 'malware'],
        'description': 'CBL + customised NJABL. 3rd party exploits (proxies, '
                       'trojans, etc.)',
    },
    '127.0.0.7': {
        'tags': ['exploit', 'malware'],
        'description': 'CBL + customised NJABL. 3rd party exploits (proxies, '
                       'trojans, etc.)',
    },
    '127.0.0.9': {
        'tags': 'hijacked',
        'description': 'Spamhaus DROP/EDROP Data',
    },
    '127.0.0.10': {
        'tags': ['end-user', 'residential'],
        'description': 'IP ranges which should not be delivering unauthenticated SMTP email.'
    },
    '127.0.0.11': {
        'tags': ['end-user', 'residential'],
        'description': 'IP ranges which should not be delivering unauthenticated SMTP email.'
    }
}

