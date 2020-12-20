from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from app.models import Todo


class TodoViewSet(ViewSet):
    def list(self, request):
        todo_objs = Todo.retrieve_all()
        todos = []
        for todo_obj in todo_objs:
            todos.append(todo_obj.to_dict())
        return Response({
            "status": "success",
            "todos": todos
        })

    def create(self, request):
        try:
            todo_obj = Todo(request.data)
            todo_obj = todo_obj.create()
            todo = todo_obj.to_dict()
        except KeyError:
            return Response({
                    "status": "error",
                    "message": "Form fields are not set properly" 
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValueError:
            return Response({
                    "status": "error",
                    "message": "form values not formatted properly"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response({
                "status": "success",
                "todo": todo
            },
            status=status.HTTP_201_CREATED
        )

    def retrieve(self, request, pk=None):
        try:
            todo_obj = Todo.retrieve(pk)
            todo = todo_obj.to_dict()
        except KeyError:
            return Response({
                    "status": "error",
                    "message": "Invalid ID"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValueError:
            return Response({
                    "status": "error",
                    "message": "No task found for provided ID"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response({
            "status": "success",
            "todo": todo
        })

    def update(self, request, pk=None):
        try:
            todo_obj = Todo(request.data)
            todo_obj.id = pk
            todo_obj.update()
            todo = todo_obj.to_dict()
        except KeyError:
            return Response({
                    "status": "error",
                    "message": "Either invalid ID or form fields not formatted properly"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValueError:
            return Response({
                    "status": "error",
                    "message": "No task found for provided ID"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response({
                "status": "success",
                "todo": todo
            },
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, pk=None):
        try:
            todo_obj = Todo(request.data)
            todo_obj.id = pk
            todo_obj = todo_obj.partial_update()
            todo = todo_obj.to_dict()
        except KeyError:
            return Response({
                    "status": "error",
                    "message": "Either invalid ID or form fields not formatted properly"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValueError:
            return Response({
                    "status": "error",
                    "message": "No task found for provided ID"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response({
                "status": "success",
                "todo": todo
            },
            status=status.HTTP_201_CREATED
        )

    def destroy(self, request, pk=None):
        try:
            Todo.delete(pk)
        except KeyError:
            return Response({
                    "status": "error",
                    "message": "Invalid ID"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response({
                    "status": "error",
                    "message": "No task found for provided ID"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as err:
            print(f"Unexpected error occured while deleting task with id {pk}, Error: {err}")
        return Response(status=status.HTTP_204_NO_CONTENT)
