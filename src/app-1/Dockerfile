FROM python:3.11
RUN mkdir -p /python-app-1
ADD app.py /python-app-1
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD ["python", "/python-app-1/app.py"]
