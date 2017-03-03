from pymongo import MongoClient

from datetime import datetime



client=MongoClient()

client = MongoClient('localhost', 27017)

db=client["kone_database"]

coll=db["floor_estimation"]



def insert(id,source,destination):

    val={

        "user":id,

        "entry_floor":source,

        "exit_floor":destination,

        "time":datetime.now().hour*60+datetime.now().minute

    }

    coll.insert_one(val)



def find(id,source):

    val={

        "user":id,

        "entry_floor":source

    }

    cur=coll.find_one(val)

    if cur==None:

        return -1

    return cur["exit_floor"]



#insert(1,2,3)

#print find(1,3)
