import json
from notebook.auth import passwd
import os
jupyter = "jupyter_notebook_config"

 
def congfig_setting(pswHash,f,fileName):
    data = json.load(open('./d.json'))
    userPort = int(data['users'][len(data['users'])-1]['port'])+1
    _id = fileName
    userPort = str(userPort)
    newData = {
        "id":_id,
        "port":userPort
    }
    data["users"].append(newData)
    print("insert:",data)
    ip = "c.NotebookApp.ip ='*'" 
    browser = "c.NotebookApp.open_browser = False"
    port = "c.NotebookApp.port =" + str(userPort)
    password = "c.NotebookApp.password =" +"\'"+ pswHash+"\'"
    f.write(ip +"\n"+ browser + "\n" + password +"\n" + port)
    print(ip +"\n"+ browser + "\n" + password + "\n"+ port)
    d = open('./d.json', "w+")                
    data = str(data).replace("'", "\"")
    d.write(data)
    print("save!")
    return fileName , port
    
def run_jupyter_user_server(fileName,port):
    cmd = 'jupyter notebook --config'+ jupyter + "_" + fileName + ".py --allow-root"
    os.system(cmd)
    print(fileName + 'your port:'+ port)
    
print('please enter your user ID:')
userId = input()
fileName = userId
print('please enter your user Password:')
psw = input()
hashpwd = passwd(psw)
if os.path.exists(jupyter+"_"+fileName+".py"):
        print(userId + "EXISTS")
else:
    with open(jupyter+"_"+fileName+".py","wt") as f:                 
        congfig_setting(hashpwd,f,fileName)
        
run_jupyter_user_server(fileName,userId)