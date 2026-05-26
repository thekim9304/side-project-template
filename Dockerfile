FROM jupyter/scipy-notebook:latest

WORKDIR /home/jovyan/project

COPY jupyter_config/overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/home/jovyan/project"
ENV PROJECT_ROOT="/home/jovyan/project"
