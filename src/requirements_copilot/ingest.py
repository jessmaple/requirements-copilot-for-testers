from pathlib import Path
# import pathlib libary, it is a module that object-oriented way to work with filesystem paths instead of treating them as plain strings.

SAMPLE_DOCS_DIR = Path("data/sample_docs")
#Points to the folder

def load_documents() -> list[str]:
    texts = []
    for path in SAMPLE_DOCS_DIR.glob("*.txt"):
        with path.open("r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts 