def _print(args, variables, *args_, **kwargs):
    if None not in args:
        print(' '.join(args))