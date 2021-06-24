def check_input(inp, lst, case_sensitive = False, verbose = True):
    """
    Check if input is in the list of options.

    Args:
        (str) inp - user input to check
        (list) lst - list of options to choose from
    Returns:
        (str) out - selected option from list or None
    """

    if not isinstance(inp, str): inp = str(inp)
    assert len(inp) > 0, 'Input must not be an empty string'
    assert isinstance(lst, list), 'Input must be non-empty list'
    for i in range(len(lst)):
        if not isinstance(lst[i], str): lst[i] = str(lst[i])
        assert len(lst[i]) > 0, 'List must not include empty strings'

    found_options = []

    for inp_check in lst:
        if inp_check.startswith(inp) or not case_sensitive and inp_check.lower().startswith(inp):
            found_options.append(inp_check)
    
    if len(found_options) == 0:
        out = None
        if verbose: print("Your answer doesn't fit to any option. Please try again.")
    elif len(found_options) == 1:
        out = found_options[0]
        if verbose: print('OK, you have chosen ' +  out + '.')
    else:
        out = None
        if verbose: print('Your answer fits to multiple options ({}). Please try again.'.format(', '.join(f for f in found_options)))
    return out
