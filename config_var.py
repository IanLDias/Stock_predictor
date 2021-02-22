from datetime import date
import requests

api_key = '4507b4f67ba846e7b9a35228be9a69ae'


start_date = "2014-01-01"
today = date.today().strftime("%Y-%m-%d")

#Steps to update:
#1) Save code to github
#2) Connect to EC2 instance
#    ssh -i "streamlit_app.pem" ubuntu@ec2-18-189-184-147.us-east-2.compute.amazonaws.com
#3) git clone repo
#4) Delete/update docker on the VM

