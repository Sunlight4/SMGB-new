keyFile=open("music-list.txt", "r")
keys=keyFile.readlines()
kvs=[x.split(" : ") for x in keys]
keyDict={}
for k, v in kvs:
    keyDict[k]=v
def get_resource_path(key):
    return keyDict[key]
