from pathlib import Path

def entries(path: str|Path) -> list[str]: return sorted(p.name for p in Path(path).iterdir())
def files(path: str|Path) -> list[str]: return sorted(p.name for p in Path(path).iterdir() if p.is_file())
def dirs(path: str|Path) -> list[str]: return sorted(p.name for p in Path(path).iterdir() if p.is_dir())
