import os
import io
import json
import requests

from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    Http404
)
from django.urls import reverse


def get_api_root(request):
    web_root = request.scheme + "://" + request.get_host()
    print(f"web_root: {web_root}")
    api_root = web_root + "/api/v1/todos/"
    print(f"api_root: {api_root}")
    return api_root

# Create your views here.
def index(request):
    if request.method == "GET":
        url = get_api_root(request)
        response = requests.get(url)
        if response.status_code == 200:
            # results = json.loads(response.content)
            results = response.json()
            finished = []
            todos = []
            for task in results["todos"]:
                completed = task["completed"]
                if completed == "true" or completed == "True" or  completed == True:
                    finished.append(task)
                else:
                    todos.append(task)
            context = {}
            if len(todos) > 0:
                context["todos"] = todos
            if len(finished) > 0:
                context["finished"] = finished
            return render(request, "web/index.html", context)
        else:
            return HttpResponseBadRequest("Bad Request")
    return HttpResponseBadRequest(
        'This view can not handle method {0}'.format(request.method),
        status=405
    )

def create(request):
    if request.method == "GET":
        task = {
            "title": "",
            "description": "",
            "form_goal": "Add to Todo List"
        }
        return render(request, "web/task_form.html", {"task": task})
    if request.method == "POST":
        title = request.POST["title"].strip()
        description = request.POST["description"].strip()
        if title == "" or description == "":
            return HttpResponseBadRequest("Invalid value(s) received of title or description or both.")
        url = get_api_root(request)
        data = {
            "title": title,
            "description": description,
            "completed": "false" # default value
        }
        response = requests.post(url, json=data, headers={"Connection": "close"})
        results = response.json()
        if response.status_code == 201: # i.e. HTTP 201 Created
            todo_id = results["todo"]["id"]
            print(f"the id of todo which has been updated: {todo_id}")
            return HttpResponseRedirect(reverse('web:detail', args=(todo_id,)))
        else: # i.e. HTTP 400 Bad Request
            return HttpResponseBadRequest(results["message"])
    return HttpResponseBadRequest(
        'This view can not handle method {0}'.format(request.method),
        status=405
    )

def detail(request, todo_id):
    if request.method == "GET":
        url = get_api_root(request) + todo_id + "/"
        response = requests.get(url)
        results = response.json()
        if response.status_code == 200: # HTTP 200 Content Found
            task = results["todo"]
            completed = task["completed"]
            task["title"]  = task["title"].strip()
            task["description"] = task["description"].strip()
            if completed == "true" or completed == "True" or  completed == True:
                task["status"] = "Finished"
                task["status_color"] = "success"
                task["mark_as"] = "Todo"
                task["mark_as_bool"] = "false"
            else:
                task["status"] = "Todo"
                task["status_color"] = "warning"
                task["mark_as"] = "Finished"
                task["mark_as_bool"] = "true"
            return render(request, "web/detail.html", {"task": task})
        elif response.status_code == 400: # i.e. HTTP 400 Bad Request
            return HttpResponseBadRequest(results["message"])
        else: # Now, only 404 left i.e. HTTP 404 Not Found
            raise Http404("task with provided ID not found")
    return HttpResponseBadRequest(
        'This view can not handle method {0}'.format(request.method),
        status=405
    )

def update(request, todo_id):
    if request.method == "GET":
        url = get_api_root(request) + todo_id + "/"
        response = requests.get(url, headers={"Connection": "close"})
        results = response.json()
        if response.status_code == 200:
            task = results["todo"]
            task["form_goal"] = "Update"
            return render(request, "web/task_form.html", {"task": task})
        elif response.status_code == 400: # i.e. HTTP 400 Bad Request
            return HttpResponseBadRequest(results["message"])
        else: # Now, only 404 left i.e. HTTP 404 Not Found
            raise Http404(results["message"])
    if request.method == "POST" or request.method == "PUT" or request.method == "PATCH":
        data = {}
        if "title" in request.POST:
            data["title"] = request.POST["title"]
        if "description" in request.POST:
            data["description"] = request.POST["description"]
        if "completed" in request.POST:
            data["completed"] = request.POST["completed"]
        url = get_api_root(request) + todo_id + "/"
        response = requests.patch(url, json=data)
        results = response.json()
        if response.status_code == 201: # i.e. HTTP 201 Created
            todo_id = results["todo"]["id"]
            print(f"the id of todo which has been updated: {todo_id}")
            return HttpResponseRedirect(reverse('web:detail', args=(todo_id,)))
        elif response.status_code == 400: # i.e. HTTP 400 Bad Request
            return HttpResponseBadRequest(results["message"])
        else: # Now, only 404 left i.e. HTTP 404 Not Found
            raise Http404(results["message"])
    return HttpResponseBadRequest(
        'This view can not handle method {0}'.format(request.method),
        status=405
    )


def update_status(request, todo_id):
    if request.method == "POST":
        completed = request.POST["completed"]
        url = get_api_root(request) + todo_id + "/"
        response = requests.patch(url, json={"completed": completed}, headers={"Connection": "close"})
        results = response.json()
        if response.status_code == 201: # i.e. HTTP 201 Created
            todo_id = results["todo"]["id"]
            print(f"the id of todo which status has been updated: {todo_id}")
            return HttpResponseRedirect(reverse('web:detail', args=(todo_id,)))
        elif response.status_code == 400: # i.e. HTTP 400 Bad Request
            return HttpResponseBadRequest(results["message"])
        else: # Now, only 404 left i.e. HTTP 404 Not Found
            raise Http404(results["message"])
    return HttpResponseBadRequest(
        'This view can not handle method {0}'.format(request.method),
        status=405
    )

def delete(request, todo_id):
    if request.method == "POST":
        url = get_api_root(request) + todo_id + "/"
        response = requests.delete(url, headers={"Connection": "close"})
        if response.status_code == 204: # i.e. HTTP 204 No Content
            print(f"the id of todo which has been deleted: {todo_id}")
        return HttpResponseRedirect(reverse('web:index', args=()))
    return HttpResponseBadRequest(
        'This view can not handle method {0}'.format(request.method),
        status=405
    )