from orange._parser import parse
import sys
import os
import click

variables = {}
functions = {}

@click.command()
@click.argument('filename')
def run(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            code = f.read()
        
        parse(code, variables, functions)
        sys.exit()

    click.echo('file not found')

if __name__ == '__main__':
    run()