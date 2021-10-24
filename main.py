import requests
import os
from pprint import pprint
import time
#task1
def who_smartest():
    token = '2619421814940190'
    hero_list = ['Hulk','Captain America','Thanos']
    hero_dict = {}
    for i in hero_list:
        url = f"https://superheroapi.com/api/{token}//search/{i}"
        response = requests.get(url)
        hero_dict[i] = int(response.json()['results'][0]['powerstats']['intelligence'])
    return list(hero_dict.keys())[list(hero_dict.values()).index(max(hero_dict.values()))]


#task2
class YaUploader:
    def __init__(self, token: str,path_to_file: str):
        self.token = token
        self.path_to_file=path_to_file

    def _headers(self):
        return { "Accept": "application/json", "Authorization": f"OAuth {self.token}"}

    def _open_file(self):
        return os.path.basename(self.path_to_file)

    def _upload_link(self):
        url=f"https://cloud-api.yandex.net/v1/disk/resources/upload"
        param={"path": self._open_file(),'overwrite': "true"}
        response = requests.get(url, headers=self._headers(), params=param)
        return response.json()

    def upload(self):
        response= requests.put(self._upload_link().get('href',''), data=open(self.path_to_file,'rb'))
        if response.status_code==201:
            return ('File upload!!!')
        else:
            return (f"Oops, status code is {response.status_code}")


#task3

def stac_questions():
    url = 'https://api.stackexchange.com/2.3/questions'
    params={'order': 'desc','min': (round(time.time())-172800), 'max': round(time.time()), 'sort': 'activity', 'tagged': 'python', 'site': 'stackoverflow' }
    response = requests.get(url, params=params)
    questions_dict= {}
    for i in range(len(response.json()['items'])):
        questions_dict[response.json()['items'][i]['owner']['display_name']]=response.json()['items'][i]['title']
    return(questions_dict)




if __name__=='__main__':
    #task1
    print(who_smartest())
    #task2
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = fr'{input("Input path to file with filename: ")}' #Example - D:\Users\some_path\some_txt_file.txt
    token = fr"{input('Input TOKEN: ')}"
    uploader = YaUploader(token,path_to_file)
    result = uploader.upload()
    print(result)
    #task3
    pprint(stac_questions())



