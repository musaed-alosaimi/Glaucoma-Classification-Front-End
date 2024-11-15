from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# Mount the "static" folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_html_form():
    html_content = open("./templates/index.html").read()
    return HTMLResponse(content=html_content)