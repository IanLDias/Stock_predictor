from datetime import date
import requests

api_key = '4507b4f67ba846e7b9a35228be9a69ae'


start_date = "2014-01-01"
today = date.today().strftime("%Y-%m-%d")

#Steps to update:
#1) Save code to github
#2) Connect to EC2 instance
#    ssh -i "streamlit_app.pem" ubuntu@ec2-####.us-east-2.compute.amazonaws.com
#3) Remove current remove (rm -rf <name>), git clone new repo
#4) Delete/update docker on the VM
#5) docker image build -t streamlit:app
#   Delete current container
#       docker container ls -a
#       Delete contaiber by id: docker container rm <container id> 
#6) docker container run -p 8501:8501 -d streamlit:app

