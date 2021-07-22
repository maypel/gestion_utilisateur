import typer

app = typer.Typer()

def main(extension: str= typer.Argument(..., help="Extension à chercher"), delete: bool = typer.Option(False, help="supprime les fichiers trouvés")):
    """Trouver les fichiers trouvées avec l'extension de fichier
    """

    # with typer.progressbar()
    ext = typer.style(f"{extension}", bold=True, bg=typer.colors.BLUE, fg=typer.colors.RED, underline=True)
    typer.echo(f"Recherche des fichiers avec l'extension {ext}")
    if delete:
        confirm = typer.confirm("Souhaitez vous vraiment supprimer les fichiers ?")
        if not confirm:
            typer.echo("On annule l'opération.")
            raise typer.Abort()

@app.command("search")
def search_py():
    main(extension="txt", delete=False)

@app.command("delete")
def delete_py():
    main(extension="py", delete=True)



if __name__== "__main__":
    app()
