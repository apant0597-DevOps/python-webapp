# start by pulling the python image
FROM python:3.12.1-alpine

# copy every content from the local file to the image
COPY pythonApp/* /app/

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]