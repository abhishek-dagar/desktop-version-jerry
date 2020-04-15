import os
import json
dir=r"C:\Users\dagar\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"
dir1 = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
def apps(dir):
    lst = []
    apps_name_path={}
    for item in os.listdir(dir):
        dir1 = dir
        if item in lst:
            continue
        elif os.path.isfile(os.path.join(dir, item)):
            lst.append(item)
            item1=item.replace('.ini','').replace('.lnk','')
            apps_name_path[item1]=dir+"\\"+item

        else:
            dir1 = dir1 + "\\" + item
            for itm in os.listdir(dir1):
                if itm in lst:
                    continue
                elif os.path.isfile(os.path.join(dir1, itm)):
                    lst.append(itm)
                    itm1=itm.replace('.ini','').replace('.lnk','')
                    apps_name_path[itm1] = dir1 + "\\" + itm
    return lst,apps_name_path

l1,dict1=apps(dir)
l2,dict2=apps(dir1)

l=l1+l2

dict1.update(dict2)

with open('apps.json','w') as f:
    json.dump(dict1,f,indent=4,separators=(',',':'))
