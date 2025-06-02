import os
from PoStandartu.http_utils import Response

def return_static_file(file_path):
    with open(os.path.join(file_path), "r") as f:
            return f.read() 

def return_static_directory(dir_path):
     files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
     return f"<html>" \
     "<head>" \
     f"<title> {dir_path} </title>" \
     "</head>" \
     "<body>" \
     f"<h1> {dir_path} </h1>" \
     "<ul>" \
     f"{"".join(f"<li><a href=\"{f}\">{f}</a></li>" for f in files)}" \
     "</ul>" \
     "</body>" \
     "</html>"

class StaticAction:
    def __init__(self, static_path):
        self.static_path = static_path

    def match(self, request):
        real_path = os.path.join(self.static_path, *request.path_params)
        return os.path.exists(real_path)
    
    def action(self, request):
        real_path = os.path.join(self.static_path, *request.path_params)
        if os.path.isdir(real_path):
            return Response(status_code=200, content=return_static_directory(real_path), headers={"Content-Type": "text/html"})
        else:
            return Response(status_code=200, content=return_static_file(real_path), headers={"Content-Type": "text/html"})