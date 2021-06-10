import typer
from ssg.site import Site

def __main__(source = "content", dest = "dist"):
    config = {"config": "source", "dest": "dest"}

    Site(**config)
    build()


typer.run(__main__)