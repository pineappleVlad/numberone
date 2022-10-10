import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, name_file, file_path: str):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        api_base_url = "https://cloud-api.yandex.net/"
        path_files = requests.get(api_base_url + 'v1/disk/resources/upload', params={'path': '/images/' + name_file},
                                  headers=headers)
        upload_url = path_files.json()['href']
        print(upload_url)
        r = requests.put(upload_url, headers=headers, files={'file': open(file_path, 'rb')})
        return 'Файл загружен'



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = ""
    file_name = ""
    path_to_file = os.path.abspath(file_name)
    uploader = YaUploader(token)
    result = uploader.upload(file_name, path_to_file)
    print(result)
