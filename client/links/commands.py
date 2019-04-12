import click


@click.group('links')
def links_group():
    """Interact with links like list links"""
    pass


@click.command('list')
def list_links():
    """List all links on the go server"""
    pass


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
    print('hello')


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
