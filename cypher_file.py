from pathlib import Path
from encode import encrypt


class CypherFile:
    def __init__(self, path):
        self.path = Path(path)

    def read(self):
        with open(self.path, 'r') as read_file:
            content = read_file.read()
        return content

    def _write(self):
        raise NotImplementedError

    def cipher(self):
        content = self.read()
        secret_content = encrypt(content)
        return secret_content

    def decypher(self):
        raise NotImplementedError


if __name__ == '__main__':
    file_path = Path().cwd() / 'text.txt'
    print(repr(file_path), Path.is_file(file_path))
    data_file = CypherFile(file_path).cipher()
    print(data_file)
