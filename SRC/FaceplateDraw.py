from PIL import Image, ImageDraw, ImageFont
from configs import *
import os

configFaceplates = ConfigManager()

def DrawTag(equipament:str, tag:str, description:str):

    models_path = configFaceplates.FaceplatesPath + equipament
    
    # Check if the equipament exists in the database
    if (not os.path.exists(models_path)):
        print("[ERROR] Equipament do not found")
        print(f"confirm if the name '{equipament}' is correct or add this equipament in database")
        return False
    
    # Draw the tag on each faceplate
    for tab in configFaceplates.tabs:
        try:
            img = Image.open(models_path + "/" + tab)
            image = ImageDraw.Draw(img)

            # Configure the position of tags on the faceplate
            width, height = img.size
            CenterX = width * configFaceplates.relativePosX
            pos1 = (CenterX, configFaceplates.relativePosY)
            pos2 = (CenterX, configFaceplates.relativePosY + configFaceplates.textSize + 2)

            # Draw text
            image.text(pos1, tag, fill=configFaceplates.textColor, anchor="mm")
            image.text(pos2, description, fill=configFaceplates.textColor, anchor="mm")

            #Save faceplate
            save(img, equipament, tab)
                
        except FileNotFoundError:
            continue

        except Exception as e:
            print(f"[ERROR] Fail to write Tag: {e}")
            continue


def save(img, equipament:str, tab:str) -> bool:

    try:
        # Create the equipament directory if it dont exist
        dictPath = f"Faceplates/feitos/{equipament}"
        os.makedirs(dictPath, exist_ok=True)
        
        # Save faceplate
        savePath = f"{dictPath}/{tab}"
        img.save(savePath)

        return True
    
    #Dont have space on disk or permission denied
    except OSError as e:
        print(f"[ERROR] Fail to save {equipament}. log: {e}")
        return False

    except Exception as e:
        print(f"[ERROR] Fail to save: {e}")
        return False
