from fastapi import APIRouter, HTTPException
from app.models.student import Student
from database import client,collection_student
from schemas.student import studentEntity,studentsEntity
from bson import ObjectId

route = APIRouter()
@route.get('/')
async def find_all_students():
    try:
        students = studentsEntity(collection_student.find())
        return {'status':'ok','data':students}
    except:
        return HTTPException(status_code=404, detail="Lỗi khi tìm học sinh")

@route.get('/{id}')
async def find_one_student(id):
    find = collection_student.find_one({"_id":ObjectId(id)})
    if find is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy học sinh có ID {}".format(id))
    else:
        student = studentEntity(find)
        return {'status': 'ok', 'data': student}

@route.post('/')
async def create_student(student:Student):
    new_std = collection_student.insert_one(dict(student))
    if new_std.acknowledged:
        return {'message':f'Học sinh {student.name} vừa được tạo',
                'data': studentsEntity(collection_student.find())}
    return HTTPException(status_code=404, detail="Có lỗi khi tạo học sinh")

@route.put('/')
async def update_student(id: str, student:Student):
    try:
        result = collection_student.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(student)
        })
        return {'message' : 'Sửa học sinh thành công',
                'data': studentEntity(collection_student.find_one({"_id":ObjectId(id)}))}
    except:
        raise HTTPException(status_code=404, detail="Không tìm thấy học sinh có ID {}".format(id))

@route.delete('/{id}')
async def delete_student(id):
    result = collection_student.delete_one({'_id':ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": 'Xóa học sinh thành công',
                'data': studentsEntity(collection_student.find())}
    return HTTPException(status_code=404, detail="Không tìm thấy học sinh có ID {}".format(id))
