from pathlib import Path

class Site:

    def __init__(self, source, dest):

        self._source = Path(source)
        self._source = Path(dest)

    def create_dir(self):
        directory = f"{self.dest}/{relative_to(self.source)}"
        directory.mkdir(parents=True, exists_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exists_ok=True)
        
        for path in self.source.rglob("*")
            
            if path.isdir(): 
                create_dir(path)