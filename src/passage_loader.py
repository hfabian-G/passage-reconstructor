def load_passage(path: str):
    passage = ''
    with open(path, 'r') as file:
        passage = file.read()
    return passage