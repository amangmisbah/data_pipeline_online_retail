#!/bin/bash
fileid="1UyMh6t6SmePnwh46QmnQaK5rgi3EMHZB"
filename="OnlineRetail.csv"
html=$(curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}")
curl -Lb ./cookie "https://drive.google.com/uc?export=download&$(echo ${html} | grep -Po '(confirm=[a-zA-Z0-9\\-_]+)')&id=${fileid}" -o "/opt/airflow/dags/include/${filename}"
