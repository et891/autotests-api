import grpc

import course_service_pb2
import course_service_pb2_grpc
import user_service_pb2
import user_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')

# === UserService ===
user_stub = user_service_pb2_grpc.UserServiceStub(channel)
user_response = user_stub.GetUser(
    user_service_pb2.GetUserRequest(username="Alice")
)
print(user_response.message)

# === CourseService ===
course_stub = course_service_pb2_grpc.CourseServiceStub(channel)
course_response = course_stub.GetCourse(
    course_service_pb2.GetCourseRequest(course_id="API-101")
)

print(course_response.course_id)
print(course_response.title)
print(course_response.description)
