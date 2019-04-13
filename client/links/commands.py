import click
import requests
from database import get


@click.group('links')
def links_group():
    """Interact with links like list links"""
    pass


@click.command('list')
def list_links():
    """List all links on the go server"""
    r = requests.get(f'{get.get_server_url()}/links')
    data = r.json()

    if data:
        click.echo('ID\tName\t\tURL')
        for link in data['links']:
            click.echo(
                f'{link["link_id"]}\t{link["link_name"]}\t{link["link_url"]}')


links_group.add_command(list_links)


@click.group('link')
def link_group():
    """Interact with a link like create, modify or delete"""
    pass


@click.command('create')
@click.argument('name')
@click.argument('url')
def create_link(name, url):
    """Create a link on the go server that you can use later"""
    try:
        payload = {'link_name': name, 'link_url': url}
        r = requests.post(f'{get.get_server_url()}/link', json=payload)

        r.raise_for_status()

        click.echo('Successfully created a link')

        data = r.json()

        click.echo(f'Link ID: {data["link"]["link_id"]}')
        click.echo(f'Link Name: {data["link"]["link_name"]}')
        click.echo(f'Link URL: {data["link"]["link_url"]}')

    except Exception as e:
        click.echo(f'There was an error creating a link ({e})')


@click.command('delete')
@click.argument('name')
def delete_link(name):
    """Delete a link from the go server"""
    pass


@click.command('modify')
@click.argument('name')
@click.argument('url')
def modify_link(name, url):
    """Modify a link on the go server"""
    click.echo(name, url)


link_group.add_command(create_link)
link_group.add_command(delete_link)
link_group.add_command(modify_link)
