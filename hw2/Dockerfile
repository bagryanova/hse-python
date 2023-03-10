FROM python:3.9.7
RUN apt-get update
RUN apt-get install texlive-latex-base -y && apt-get install graphviz -y
RUN mkdir artifacts/
RUN pip3 install -i https://test.pypi.org/simple/ ast-builder==1.5
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py main.py
CMD [ "python3", "main.py"]