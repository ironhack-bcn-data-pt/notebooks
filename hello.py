
import click


@click.command()
@click.argument('name', default='friend')
@click.argument('lang', default='en')
def hello(name, lang):
    if lang == 'en':
        print(f'Hi, {name}')
    elif lang == 'es':
        print(f'Hola, {name}')
    else:
        print(f'Hi, {name}')

 
if __name__ == '__main__':
    hello()