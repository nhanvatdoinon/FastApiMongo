def studentEntity(item) -> dict:
    return {
        "id" : str(item['_id']),
        "name" : item['name'],
        "address": item['address'],
        "email": item['email'],
        "phone": item['phone'],
        "age": item['age'],
        "gpa": item['gpa'],
    }

def studentsEntity(entity) -> dict:
    return [studentEntity(item) for item in entity]