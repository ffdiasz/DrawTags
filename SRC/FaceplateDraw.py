from PIL import Image, ImageDraw, ImageFont
import os

#configs
textSize = 10
relativePosX = 0.5
relativePosY = 15
textColor = (255,255,255) #white

def DrawTag(equipament:str, tag:str):

    path = "Faceplates/Models/" + equipament
    
    if (not os.path.exists(path)):
        print("[ERROR] Equipament do not found")
        print(f"confirm if the name '{equipament}' is correct or add this equipament in database")
        return False
    
    tabs:str = ["ALARMS.png", "ASSETINFO.png", "HOME.png", "TRENDS.png"]

    for tab in tabs:
        try:
            img = Image.open(path + "/" + tab)
            image = ImageDraw.Draw(img)

            # Configure the position of tags on the faceplate
            width, height = img.size
            CenterX = width * relativePosX
            pos1 = (CenterX, relativePosY)
            pos2 = (CenterX, relativePosY + textSize + 2)

            # Draw text
            image.text(pos1, tag, fill=textColor, anchor="mm")
            image.text(pos2, tag, fill=textColor, anchor="mm")

            #Save faceplate
            save(img, equipament, tab)
                
        except FileNotFoundError:
            continue

        except Exception as e:
            print(f"[ERROR] unexpected error: {e}")
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
        print(f"[ERROR] Unespected error: {e}")
        return False
