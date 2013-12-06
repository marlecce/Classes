
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades


def find():

    print ""

    query = {'type':'homework'}

    try:
        cursor = grades.find(query).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING) ])
        count = 1
        for doc in cursor:
        		print ""
        		if count % 2 != 0:
        			print doc, " removed"
        			query = {'type':'homework', '_id': doc['_id']}
        			print grades.remove(query)        			
        		print doc
        		count += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]

find()

