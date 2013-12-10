
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
data=db.students

def find():

    print ""

    try:
        cursor = data.find({"scores.type": "homework"})
        for student in cursor:
    			homeworkScore = []
    			for score in student['scores']:
        			if score["type"] == "homework":
        				homeworkScore.append(score["score"])
    			db.students.update({"_id": student["_id"]}, {"$pull": {"scores": {"score": min(homeworkScore)}}})
        							
    except:
        print "Unexpected error:", sys.exc_info()[0]

find()

