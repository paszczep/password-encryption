from pathlib import Path
from encode import encrypt, decrypt


class CypherFile:
    def __init__(self, path):
        self.path = Path(path)
        self.content = str()

    def _read(self):
        with open(self.path, 'r') as read_file:
            self.content = read_file.read()

    def _write(self):
        with open(self.path, 'w') as write_file:
            write_file.write(self.content)

    def cipher(self):
        self._read()
        self.content = encrypt(self.content)
        self._write()

    def decypher(self):
        self._read()
        self.content = decrypt(self.content)
        self._write()


if __name__ == '__main__':
    file_path = Path().cwd() / 'text.txt'
    CypherFile(file_path).decypher()
