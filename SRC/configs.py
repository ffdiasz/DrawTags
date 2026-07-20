import json

class ConfigManager:
    def __init__(self, 
                 config_file1="Configs/faceplateConfigs.json",
                 config_file2="Configs/pathConfigs.json"):
        
        # 1. Carregando Faceplates com segurança
        try:
            with open(config_file1, 'r') as f:
                faceplatesConfig = json.load(f)
                
            self.textSize:int = faceplatesConfig.get("textSize", 0)
            self.relativePosX:int = faceplatesConfig.get("relativePosX", 0)
            self.relativePosY:int = faceplatesConfig.get("relativePosY", 0)
            self.textColor:tuple = tuple(faceplatesConfig.get("textColor", (0, 0, 0)))
            self.tabs:str = faceplatesConfig.get("tabs", [])
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"[AVISO] Falha ao ler {config_file1}. Usando valores padrão. Erro: {e}")
            # Se der erro, aplicamos os valores padrão diretamente
            self.textSize:int = 0
            self.relativePosX:int = 0
            self.relativePosY:int = 0
            self.textColor:int = (0, 0, 0)
            self.tabs:str = []

        # 2. Carregando Paths com segurança
        try:
            with open(config_file2, 'r') as f:
                pathsConfig = json.load(f)
                
            self.csvPath = pathsConfig.get("csvPath", "")
            self.FaceplatesPath = pathsConfig.get("FaceplatesPath", "")
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"[AVISO] Falha ao ler {config_file2}. Usando valores padrão. Erro: {e}")
            self.csvPath = ""
            self.FaceplatesPath = ""