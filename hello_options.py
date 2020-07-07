import click

@click.command()
@click.option('--name', default='friend')
@click.option('--lang', default='en')
def main(name, lang):
    if lang == 'en':
        print(f'Hi, {name}')
    elif lang == 'es':
        print(f'Hola, {name}')
    else:
        print(f'Hi, {name}')

 
if __name__ == '__main__':
    main()