from concurrent import futures  # Импорт пула потоков для асинхронного выполнения

import grpc  # Импорт библиотеки gRPC

import course_service_pb2
import course_service_pb2_grpc
import user_service_pb2  # Сгенерированные классы для работы с gRPC-сообщениями
import user_service_pb2_grpc  # Сгенерированный класс для работы с сервисом


# Реализация gRPC-сервиса
class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    """Реализация методов gRPC-сервиса UserService"""

    def GetUser(self, request, context):
        """Метод GetUser обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetUser от пользователя: {request.username}')

        # Формируем и возвращаем ответное сообщение
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}!")

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса CourseService"""

    def GetCourse(self, request, context):
        """Метод GetUser обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetUser от пользователя: {request.course_id}')
        title = "Автотесты API"
        description = "Будем изучать написание API автотестов"
        # Формируем и возвращаем ответное сообщение
        return course_service_pb2.GetCourseResponse(course_id=request.course_id,
                                                    title=title,
                                                    description=description, )


# Функция для запуска gRPC-сервера
def serve():
    """Функция создает и запускает gRPC-сервер"""

    # Создаем сервер с использованием пула потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем два сервиса на одном сервере
    user_service_pb2_grpc.add_UserServiceServicer_to_server(
        UserServiceServicer(), server
    )
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server
    )

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()
