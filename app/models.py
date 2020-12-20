from django.db import models

# from firebase_admin import firestore
from todo.settings import FIRESTORE as store

# Create your models here.
class Todo(models.Model):
    # id = models.CharField(max_length=256, required=False)
    # title = models.CharField(max_length=1024, required=False)
    # description = models.TextField(required=False)
    # completed = models.BooleanField(required=False)

    fields = ["id", "title", "description", "completed"]
    collection_name = "todo"

    def __init__(self, data):
        for key, value in data.items():
            if key not in Todo.fields:
                raise KeyError
            value = value.strip()
            if value == "":
                raise KeyError
            if key == "completed" and value not in ["true", "True", True, "false", "False", False]:
                raise KeyError
            setattr(self, key, value)

    @staticmethod
    def from_id(pk=None):
        if pk == None:
            raise KeyError
        return Todo({
            "id": pk
        })

    def to_dict(self):
        ret = {}
        for key, value in self.__dict__.items():
            ret[key] = value
        return ret

    def to_dict_without_id(self):
        ret = {}
        for key, value in self.__dict__.items():
            if key == "id": continue
            ret[key] = value
        return ret

    def create(self):
        setfields = self.__dict__.keys()
        if ("title" not in setfields) or ("description" not in setfields) or ("completed" not in setfields):
            raise KeyError
        # todo_id = store.collection(Todo.collection_name).add(self.to_dict_without_id())[1].id
        # setattr(self, "id", todo_id)
        doc_ref = store.collection(Todo.collection_name).document()
        setattr(self, "id", doc_ref.id)
        doc_ref.set(self.to_dict_without_id())
        return self

    @staticmethod
    def doc_to_dict(doc):
        todo = doc.to_dict()
        todo["id"] = doc.id
        return todo

    @staticmethod
    def doc_to_todo_obj(doc):
        return Todo(Todo.doc_to_dict(doc))

    @staticmethod
    def retrieve_all():
        todos = []
        for doc in store.collection(Todo.collection_name).stream():
            todos.append(Todo.doc_to_todo_obj(doc))
        return todos

    @staticmethod
    def retrieve(pk=None):
        if pk == None:
            raise ValueError
        doc = store.collection(Todo.collection_name).document(pk).get()
        if not doc.exists:
            raise ValueError
        return Todo.doc_to_todo_obj(doc)

    def pull():
        setfields = self.__dict__.keys()
        if ("id" not in setfields):
            raise KeyError
        if ("title" in setfields) and ("description" in setfields) and ("completed" in setfields):
            return Todo(self.to_dict())
        ret = Todo.retrieve(self.id)
        for key, value in ret.__dict__.items():
            setattr(self, key, value)
        return self

    def update(self):
        setfields = self.__dict__.keys()
        if ("id" not in setfields) or ("title" not in setfields) or ("description" not in setfields) or ("completed" not in setfields):
            raise KeyError
        doc = store.collection(Todo.collection_name).document(self.id).get()
        if not doc.exists:
            raise ValueError
        store.collection(Todo.collection_name).document(self.id).set(self.to_dict_without_id())
        return self

    def partial_update(self):
        setfields = self.__dict__.keys()
        if ("id" not in setfields):
            raise KeyError
        doc = store.collection(Todo.collection_name).document(self.id).get()
        if not doc.exists:
            raise ValueError
        store.collection(Todo.collection_name).document(self.id).update(self.to_dict_without_id())
        return self

    def remove(self):
        setfields = self.__dict__.keys()
        if ("id" not in setfields):
            raise KeyError
        store.collection(Todo.collection_name).document(self.id).delete()

    @staticmethod
    def delete(pk=None):
        if pk == None:
            raise KeyError
        store.collection(Todo.collection_name).document(pk).delete()

    def __str__(self):
        return self.title
