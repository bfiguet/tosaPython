import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()

@app.command('run')
def main(extension: str,
	directory: Optional[str] = typer.Argument(None, help="Directory to search."),
	delete: bool = typer.Option(False, help="Delete found files.")):
	"""
	Show files found with given extension.

	Args:
		extension (str): _description_
		directory (Optional[str], optional): _description_. Defaults to typer.Argument(None, help="Directory to search.").
		delete (bool, optional): _description_. Defaults to typer.Option(False, help="Delete all files.").
	"""

	if directory:
		directory = Path(directory)
	else:
		directory = Path.cwd()
	
	if not directory.exists():
		typer.secho(f"Directory '{directory}' don't exist.", fg=typer.colors.RED)
		raise typer.Exit()
	
	files = directory.rglob(f"*.{extension}")
	
	if delete:
		typer.confirm("Do you really want to delete files ?", abort=True)
		for file in files:
			file.unlink()
			typer.secho(f"file deletion {file}", fg=typer.colors.RED)
		#else:
		#	typer.echo("No files were found")
	else:
		typer.secho(f"File find with .{extension}: ", bg=typer.colors.BRIGHT_BLUE, fg=typer.colors.BRIGHT_WHITE)
		for file in files:
			typer.echo(file)
		#else:
		#	typer.echo("No files were found")
		
@app.command()
def search(extension: str):
	"""
	search for files with the data extension.

	Args:
		extension (str): _description_
	"""
	main(extension=extension, directory=None, delete=False)

@app.command()
def delete(extension: str):
	"""
	delete files with given extension.

	Args:
		extension (str): _description_
	"""
	main(extension=extension, directory=None, delete=True)


if __name__ == "__main__":
	#typer.run(main)
	app()