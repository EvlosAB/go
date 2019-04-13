#!/usr/bin/env python3

import click
from database.db import session, create_database, drop_database
from database.models import Setting
from links import commands as links
from tokens import commands as tokens

VERSION = 'go cli 1.0.0'


@click.group(invoke_without_command=True)
@click.option('--version', is_flag=True, default=False,
              help='Show the current version and exit.')
def go_cli(version):
    '''
    Go is a short-link server that allows you to make shortcuts.
    Short-link for Google might be go/google.
    '''
    if version:
        click.echo(VERSION)


@click.command('setup')
@click.argument('token-name')
@click.argument('token')
@click.argument('server-url')
def setup_cli(token_name, token, server_url):
    '''Setup go cli to work with the go server'''
    drop_database()
    create_database()

    token_name_i = Setting(
        setting_name='token_name', setting_value=token_name)
    token_i = Setting(setting_name='token', setting_value=token)
    token_url_i = Setting(setting_name='url', setting_value=server_url)

    session.add(token_name_i)
    session.add(token_i)
    session.add(token_url_i)

    session.commit()

    click.echo('Go CLI successfully setup')


@click.command('settings')
def list_settings():
    '''List settings'''
    settings = [setting for setting in session.query(Setting).all()]
    if settings:
        click.echo('Setting ID\tSetting Key\tSetting Value')
        for setting in settings:
            click.echo(
                f'{setting.setting_id}\t\t{setting.setting_name}\t\t'
                f'{setting.setting_value}')
    else:
        click.echo('No settings available')


go_cli.add_command(setup_cli)
go_cli.add_command(list_settings)

go_cli.add_command(links.link_group)
go_cli.add_command(links.links_group)

go_cli.add_command(tokens.token_group)
go_cli.add_command(tokens.tokens_group)

if __name__ == '__main__':
    go_cli()
