import click

@click.group()
def main():
    pass

@main.command()
def dos():
    print('dos')

@main.command()
def uno():
    print('uno')

 
if __name__ == '__main__':
    main()