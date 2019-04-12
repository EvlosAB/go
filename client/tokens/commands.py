import click


@click.group('tokens')
def tokens_group():
    """Commands for tokens"""
    pass


@click.command('list')
def list_tokens():
    """List all tokens on the go server (does not include the token itself)"""
    pass


tokens_group.add_command(list_tokens)


@click.group('token')
def token_group():
    """Issue and revoke tokens"""
    pass


@click.command('issue')
@click.argument('name')
@click.argument('token')
def issue_token():
    """Issue a new token"""
    pass


@click.command('revoke')
@click.argument('name')
def revoke_token():
    """Revoke a current token"""
    pass


token_group.add_command(issue_token)
token_group.add_command(revoke_token)
