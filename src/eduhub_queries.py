import pymongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from pprint import pprint

# --- SETUP: MongoDB Connection ---
def get_mongo_client(uri="mongodb://localhost:27017/", db_name="eduhub_db"):
    
    client = pymongo.MongoClient(uri)
    return client[db_name]

# ----------------------------------------------------------------------
#                         TASK 3: CRUD OPERATIONS
# ----------------------------------------------------------------------

def create_new_user(db, user_data):
    """C - Inserts a new user document into the users collection."""
    
    return db.users.insert_one(user_data) #here we use return to get the inserted_id if needed.

def get_user_by_email(db, email):
    """R - Retrieves a single user document by their email."""
    
    return db.users.find_one({"email": email})

def update_course_category(db, course_id, new_category):
    """U - Updates the category of a course by its ID."""
    ion
    return db.courses.update_one(
        {"courseId": course_id},
        {"$set": {"category": new_category}}
    )

def delete_user_and_enrollments(db, user_id):
    """D - Deletes a user and their related enrollments."""
    
    db.enrollments.delete_many({"userId": user_id})
    return db.users.delete_one({"userId": user_id})


# ----------------------------------------------------------------------
#                        TASK 4: AGGREGATION QUERIES
# ----------------------------------------------------------------------

def get_monthly_enrollment_trends(db):
    """Aggregation Pipeline 1: Calculates enrollment count by month."""
    pipeline_enrollment_trends = [
        { '$group': {
            '_id': { '$dateToString': { 'format': "%Y-%m", 'date': "$enrollmentDate" } },
            'count': { '$sum': 1 }
        } },
        { '$sort': { '_id': 1 } }
    ]
    return list(db.enrollments.aggregate(pipeline_enrollment_trends))

def get_popular_course_stats(db):
    """Aggregation Pipeline 2: Finds the top 5 most popular courses (by enrollments) 
       and retrieves their title using $lookup."""
    pipeline_enrollment_stats = [
        {'$group': {'_id': '$courseId', 'totalEnrollments': {'$sum': 1}}},
        {'$lookup': {
            'as': 'course_info',
            'foreignField': 'courseId',
            'from': 'courses',
            'localField': '_id'
        }},
        {'$unwind': '$course_info'},
        {'$project': {
            '_id': 0,
            'courseId': '$_id',
            'courseTitle': '$course_info.title',
            'totalEnrollments': 1
        }},
        {'$sort': {'totalEnrollments': -1}},
        {'$limit': 5}
    ]
    return list(db.enrollments.aggregate(pipeline_enrollment_stats))


# ----------------------------------------------------------------------
#                              EXECUTION BLOCK (for testing)
# ----------------------------------------------------------------------

if __name__ == "__main__": #this function will only run when this script is executed directly, not when imported as a module.
    # Establish MongoDB connection
    
    db = get_mongo_client()
    print("--- MongoDB Connection Established (eduhub_queries.py) ---\n")

    # --- CRUD Demonstration ---
    
    # 1. READ: Retrieve a known course's data 
    print("--- 1. R: Read Course Stats ---")
    popular_courses = get_popular_course_stats(db)
    pprint(popular_courses)

    # 2. CREATE: Add a new dummy user
    new_user_id = 'test123'  # Unique userId for testing
    new_user_data = {
        "userId": new_user_id,
        "email": "test@queries.com",
        "firstName": "Query",
        "lastName": "Test",
        "role": "student",
        "dateJoined": datetime.now(),
        "isActive": True
    }
    create_result = create_new_user(db, new_user_data)
    print(f"\n--- 2. C: New User Created ({create_result.inserted_id}) ---")

    # 3. DELETE: Clean up the dummy user
    delete_result = delete_user_and_enrollments(db, new_user_id)
    print(f"--- 3. D: Deleted User ({delete_result.deleted_count}) ---")

    # --- AGGREGATION Demonstration ---
    print("\n--- 4. Aggregation: Monthly Enrollment Trends ---")
    trends = get_monthly_enrollment_trends(db)
    pprint(trends)


    db.client.close()
    print("\n--- Connection Closed ---")