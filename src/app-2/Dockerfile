FROM python:3.11
RUN mkdir -p /python-app-2
ADD app.py /python-app-2
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD ["python", "/python-app-2/app.py"]
