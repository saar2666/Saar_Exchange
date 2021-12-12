FROM python:3.8
# 3.8 is the python version we gonna use here (in the function we aleardy did in 2.7 by mistake)
#EXPOSE 8080
ADD main.py .
ADD test_functions.py .
ADD all_currency_file_new.json .
#. mean that the file is in this directory
#RUN apt-get update
#RUN apt-get install -y build-essential
RUN pip3 install requests pytest
#which packeges to install , what we are using in the code
CMD ["python", "./main.py"]
# just run python main.py