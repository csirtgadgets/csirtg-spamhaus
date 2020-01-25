from csirtg_spamhaus import get

INDICATORS = (
    'dbltest.com',
    '71.6.146.130',
)


def test_basics():
    for i in INDICATORS:
        for p in get(i, '209.18.47.61'):
            assert p


    try:
        get('asdf')

    except ValueError:
        pass

    assert get('1.1.1.1', '209.18.47.61') is None
