#!/usr/bin/python3


import sys



def safe_function(fct, *args):

    """Executes a function safely.


    Args:

        fct: This refers to the  function to execute.

        args: These are the arguments for fct.


    Returns:

        If an error occurs - None.

        Otherwise - the result of the call to fct.

    """

    try:

        result = fct(*args)

        return (result)

    except:

        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

        return (None)
