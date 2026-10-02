FROM python:3.11-slim
WORKDIR /app
COPY inventory_manager.py .
COPY inventory.json .
CMD ["python", "inventory_manager.py"]
##docker mount and run
## docker run --rm -it -v "${PWD}:/usr/src/app" -w /usr/src/app python:3.11-slim python inventory_manager.py
##docker build -t inf1003-labs-smart-auditor .
##docker run --rm -it inf1003-labs-smart-auditor