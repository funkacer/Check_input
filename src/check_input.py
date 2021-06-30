def check_input(inp, lst, case_sensitive = False, verbose = True):
    """
    Check if input is in the list of options.

    Args:
        (str) inp - user input to check
        (list) lst - list of options to choose from
    Returns:
        (str) out - selected option from list or None
    """

    #if not isinstance(inp, str): inp = str(inp)
    assert len(str(inp)) > 0, 'Input must not be an empty string'
    assert isinstance(lst, list), 'Input must be non-empty list'
    for l in lst:
        assert len(str(l)) > 0, 'List must not include empty strings'
        assert isinstance(l, (str, int, float)), 'List must include strings, floats or integers'
        if str(l).startswith(' ') and verbose:
            print("Warning: option '{}' starts with blank.".format(l))

    found_options = []
    match = 0
    found = None

    for inp_check in lst:
        #print(inp_check.__class__)
        if isinstance(inp_check, str):
            if inp_check.startswith(inp) or not case_sensitive and inp_check.lower().startswith(inp.lower()):
                found_options.append(inp_check)
            if inp_check == inp or not case_sensitive and inp_check.lower() == inp.lower():
                match = 1
                found = inp_check
        else:
            if str(inp_check).startswith(str(inp)):
                found_options.append(str(inp_check))
            if inp_check == inp:
                match = 1
                found = inp_check

    if len(found_options) == 0:
        out = None
        if verbose: print("Your answer doesn't fit to any option('{}'). Please try again.".format("', '".join(f for f in lst)))
    elif len(found_options) == 1:
        out = found_options[0]
        if verbose: print("OK, you have chosen '{}'.".format(out))
    elif match == 1:
        out = found
        if verbose: print("OK, you have chosen '{}'.".format(out))
    else:
        out = None
        if verbose: print("Your answer fits to multiple options ('{}'). Please try again.".format("', '".join(f for f in found_options)))

    #print(match, found, found_options, lst)
    return out
