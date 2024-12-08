import os

def createKeys(path, prefix, extensions):    
    for root, dirs, files in os.walk(path):
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    path = os.path.join(root, file).replace("\\","/")
                    key = prefix + path.replace("_", ".").replace("/", ".").replace(ext, "")
                    print('"' + key + '" : "' + path + '",')
                    break
                    
                    
createKeys("loot_tables", "", [".json"])

