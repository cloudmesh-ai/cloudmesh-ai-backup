import click
from cloudmesh.ai.common.io import console

@click.command()
def backup_cmd():
    """
    Backup command that only prints to the console.
    """
    console.print("Backup command executed successfully.")

def register(cli):
    """
    Registers the backup command with the main CLI.
    """
    cli.add_command(backup_cmd, name="backup")