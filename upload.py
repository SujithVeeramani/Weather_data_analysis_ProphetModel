from fastapi import FastAPI, File, UploadFile, Form, Response, BackgroundTasks, Request
from fastapi.staticfiles import StaticFiles
import pandas as pd
from io import BytesIO
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

from model_prophet import model_prop

matplotlib.use('AGG')
app = FastAPI()


templates = Jinja2Templates(directory="templates")

global_filename = None

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("upload_form.html", {"request": request, "df_content": None, "columns": []})


@app.post("/uploadfile/")
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    file_content = BytesIO(file.file.read())
    df = pd.read_csv(file_content)

    columns = df.columns.tolist()

    return templates.TemplateResponse("upload_form.html", {"request": request, "df_content": None, "columns": columns, "file_content": file_content})


@app.post("/processfile/")
async def process_selected_columns(
    request: Request,
    selected_columns: List[str] = Form(...),
    filename: str = Form(...),
    file: UploadFile = File(...),
):
    global global_filename  

    try:
        file_content_bytes = BytesIO(file.file.read())
        df = pd.read_csv(file_content_bytes)

        selected_columns = [col.strip() for col in selected_columns]
        selected_columns = list(set(selected_columns + ['date_time', 'tempC']))
        selected_df = df[selected_columns]
        processed_filename = f"{filename}.csv"
        selected_df.to_csv(processed_filename, index=False)
        df_content = selected_df.head(10).to_html()

       
        global_filename = processed_filename

        return templates.TemplateResponse(
            "upload_form.html",
            {"request": request, "df_content": df_content, "columns": [], "file_content": file.file.read().decode()},
        )
    except Exception as e:
        print(f"Error: {e}")
        raise


def create_img():
    global global_filename
    img_buf = model_prop(global_filename)
    return img_buf

@app.get('/results', response_class=HTMLResponse)
async def get_img(request: Request, background_tasks: BackgroundTasks):
    img_path = create_img()
    background_tasks.add_task(lambda: plt.close())
    return templates.TemplateResponse("image_result.html", {"request": request, "img_path": img_path})
