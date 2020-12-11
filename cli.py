import click
from service.base_service import extract_block, extract_committee, extract_validator


@click.group()
def cli():
    pass


cli.add_command(extract_block, 'extract_block')
cli.add_command(extract_validator, 'extract_validator')
cli.add_command(extract_committee, 'extract_committee')
