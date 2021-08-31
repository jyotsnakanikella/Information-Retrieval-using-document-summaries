import json
with open("C:/Users/Hp/Documents/project/pro/model.txt", "rb") as fin:
    content = json.load(fin)
with open("C:/Users/Hp/Documents/project/pro/modelJson.txt", "wb") as fout:
    json.dump(content, fout, indent=1)
with open("C:/Users/Hp/Documents/project/pro/model1.txt", "rb") as fin:
    content = json.load(fin)
with open("C:/Users/Hp/Documents/project/pro/model1Json.txt", "wb") as fout:
    json.dump(content, fout, indent=1)
