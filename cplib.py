import os
import shutil

allF = []
newF = []
enlist = []
libDir = "wordlib/"
workDir = "/home/donspace/.config/ibus/rime/"
config_file = "luna_pinyin.my_words.dict.yaml"
label = "cplib"

# Find all yaml files
for file in os.listdir(libDir):
    if os.path.isfile(libDir + file) and file.endswith(".yaml"):
        allF.append(file)

# Translate them into rime format
for file in allF:
    names = file.split(".")
    if len(names) == 2:
        prefix = names[0]
    else:
        label = names[0]
        prefix = names[1]
    
    grasp = ""
    filePath = libDir + file
    with open(filePath, "r") as F:
        grasp = F.readline().strip("\n")
        if not grasp.startswith("---"):
            content = F.readlines()
            content = ["---\n", 
                    "name: " + label + "." + prefix + "\n", 
                    "version: 1.0\n", 
                    "sort: by_weight\n", 
                    "use_preset_vocabulary: true\n", 
                    "...\n"] + content
            Fw = open(filePath, "w")
            Fw.writelines(content)
            Fw.close()
        F.close()
    new_file = label + "." + prefix + ".dict.yaml"
    os.rename(filePath, libDir + new_file)
    newF.append(new_file)

# Move the file into rime directory
for new in newF:
    if new not in os.listdir(workDir):
        newNames = new.split(".")
        enlist.append("  - "+ newNames[0] + "." + newNames[1] + "\n")
    shutil.copy(libDir + new, workDir + new)

# Modify config
config = workDir + config_file
with open(config, "r") as F:
    content = F.readlines()
    content.pop()
    content += enlist + ["---\n"]
    F.close()
with open(config, "w") as F:
    F.writelines(content)
    F.close()
