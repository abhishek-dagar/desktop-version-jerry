import re
import os
from subprocess import check_output
import json

def get_processes_running():
    """
    #Takes tasklist output and parses the table into a dict
    """
    tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
    p = []
    for task in tasks:
        m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())
        if m is not None:
            if "exe" in m.group(1).decode():
                p.append({"image":m.group(1).decode(),
                        "pid":int(m.group(2).decode()),
                        "session_name":m.group(3).decode(),
                        "session_num":int(m.group(4).decode()),
                        "mem_usage":m.group(5).decode('ascii', 'ignore')
                        })
    return( p)
'''with open('apps.json') as  f:
    data=json.load(f)
l=[]
for key in data:
    l.append(key)'''
def apps_name_in_pc():
    with open("JSON_FILE\\apps.json") as w:
        data = json.load(w)
    with open("JSON_FILE\\microsoftapps.json") as wf:
        data1=json.load(wf)
        return data,data1
def appname():
    apps_name=[]
    lst=get_processes_running()
    data,data1=apps_name_in_pc()
    l1 = [key for key in data]
    l2 = [key for key in data1]
    lst1 = l1 + l2
    for i in range(len(lst)):
        for j in range(len(lst1)):
            nam=lst[i]['image']
            nam=nam.split(".exe")
            if nam[0].replace("64","").lower() in lst1[j].lower() or lst1[j].lower() in nam[0].replace("64","").lower():
                apps_name.append(lst[i]['image'])
            elif nam[0].replace("32","").lower() in lst1[j].lower()or lst1[j].lower() in nam[0].replace("32","").lower():
                apps_name.append(lst[i]['image'])
            elif nam[0].lower() in lst1[j].lower() or lst1[j].lower() in nam[0].lower():
                apps_name.append(lst[i]['image'])
    for i in range(len(lst)):
        if 'music' in lst[i]['image'].lower():
            apps_name.append("Music.UI.exe")
        elif 'excel' in lst[i]['image'].lower():
            apps_name.append('EXCEL.exe')
        elif 'jerry.exe' in lst[i]['image'].lower():
            apps_name.append('jerry.exe')
    apps_name=list(set(apps_name))
    return apps_name
def close_app(name):
    apps_name = appname()
    for i in range(len(apps_name)):
        if name.lower() in apps_name[i].lower() or apps_name[i].lower() in name.lower():
            name = apps_name[i]
            try:
                os.system("taskkill /F /IM "+name)
                return "closed..."
            except:
                pass
    else:
        return  "App is not opened"

def open_apps(apps_name):
    data,data1 = apps_name_in_pc()
    l1 = [key for key in data]
    lenght_apps=len(l1)
    l2 = [key for key in data1]
    l=l1+l2
    for i in range(len(l)):
        if (apps_name.lower() in l[i].lower() or l[i].lower() in apps_name.lower()) and i<=lenght_apps:
            os.startfile(data[l[i]])
            return "opening..."
        elif (apps_name.lower() in l[i].lower() or l[i].lower() in apps_name.lower()) and i > lenght_apps:
            os.system("start "+data1[l[i]])
            return "opening..."
    else:
        return "App not found"

