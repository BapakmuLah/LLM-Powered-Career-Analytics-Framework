FROM python:3.10-slim

WORKDIR /project

# COPY REQUIREMENTS & INSTALL DEPENDENCIES
COPY ./requirements.txt /project/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt


# COPY ALL YOUR FOLDER INTO CONTAINER
COPY . /project

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]