def replace_max(tpl):
    m = max(tpl)
    idx = tpl.index(m)
    print(tpl[:idx])
    print(tpl[idx + 1:])
    var = tpl[:idx] + (None,) + tpl[idx + 1:]

    return var


print(replace_max((1, 9, 3, 4)))
