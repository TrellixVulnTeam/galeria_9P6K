import os
import json
import requests
import webbrowser

class ManageConfig():
    @staticmethod
    def get_configuration_file_path():
        return os.getcwd() + "/files/configuration.json"

    @staticmethod
    def get_config():
        try:
            with open(ManageConfig.get_configuration_file_path(), "r") as file:
                return json.load(file)
        except:
            return {"status":" Erro - Não foi possível encontrar o arquivo de configuração"}

    @staticmethod
    def save_config(data):
        return True
        try:
            with open(ManageConfig.get_configuration_file_path(), "r") as file:
                data_file = json.load(file)

            for idx, obj in enumerate(data_file):
                if obj['id'] == 2:
                    data_file.pop(idx)

            file = open(ManageConfig.get_configuration_file_path(), "w")
            file.write(str(data_file))
            file.close()
            return {"status": "Arquivo salvo com sucesso"}
        except Exception as e:
            return {"status": "Erro - Não foi possível salvar o arquivo de configuração"}


class ManageApplication():
    @staticmethod
    def set_image():
        #webbrowser.open("http://127.0.0.1:8080/playimage?image=1")
        os.system("firefox --kiosk http://127.0.0.1:8080/playimage?image=1")
        # "curl -XGET 'http://127.0.0.1:5050/playimage?image=1'"
        #result = requests.get("http://127.0.0.1:8080/playimage?image=1")
        # if result.status_code == 200:
        #     return {"status": "ok"}

    @staticmethod
    def set_video():
        #webbrowser.open("http://127.0.0.1:8080/playvideo?video=1")
        os.system("firefox --kiosk http://127.0.0.1:8080/playvideo?video=1")
        #result = requests.get("http://127.0.0.1:8080/playvideo?video=1")
        # if result.status_code == 200:
        #     return {"status": "ok"}
