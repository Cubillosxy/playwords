def parenthesis_matching(string):

    if not string:
        return False

    stack = []
    wrapper_dict = {
        '{': '}',
        '[': ']',
        '(': ')',
    }

    for i in string:
        if i in wrapper_dict:
            stack.append(i)
            continue

        # jump others characters
        if i not in wrapper_dict.values():
            continue

        if not stack:
            return False

        if i in wrapper_dict.values():
            pop_element = stack.pop()
            if wrapper_dict.get(pop_element) != i:
                return False

    if not stack:
        return True

    return False


test_dict = {
    '{()}[]': True,
    '{()}[': False,
    'f(e(d))': True,
    '[': False,
    '': False,
    ')(': False,
    '(b))': False,
    '((b)': False,
    '(a[0]+b[2c[6]]){24+53}': True
}

for key, value in test_dict.items():
    print ('{} >>> {}'.format(key, value))
    assert parenthesis_matching(key) == value
