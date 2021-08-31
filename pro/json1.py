import json

f = open("C:/Users/Hp/Documents/project/pro/model.txt", 'r')
f1 = open("C:/Users/Hp/Documents/project/pro/modeljson.txt", 'w')
data = json.loads(f1)
f.write(json.dumps(data, indent=1))
f.close()
t = open("C:/Users/Hp/Documents/project/pro/model1.txt", 'r')
t1 = open("C:/Users/Hp/Documents/project/pro/model1json.txt", 'w')
data = json.loads(t1)
t.write(json.dumps(data, indent=1))
t.close()
