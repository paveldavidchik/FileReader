
import codecs


class FileReader:
    def __init__(self, file_path: str):
        self.__file_path = str(file_path)

    file_path = property()

    @file_path.setter
    def file_path(self, file_path: str):
        try:
            if not isinstance(file_path, str):
                raise ValueError('Неверный путь к файлу!')
            else:
                self.__file_path = file_path
        except ValueError as err:
            print(err)
            raise Exception from err

    @file_path.getter
    def file_path(self) -> str:
        return self.__file_path

    def read(self) -> str:
        try:
            file_read = ''
            with codecs.open(self.__file_path, encoding='utf-8') as file:
                file_read = file.read()
            return file_read
        except FileNotFoundError:
            print('Файл не существует!')
        finally:
            file.close()


fileReader = FileReader(file_path='file.txt')
print(fileReader.read())
