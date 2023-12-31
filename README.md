# DocuBot
<h3>DocuBot is an innovative chatbot application designed to process and analyze content from uploaded PDF files, <br/>
  leveraging NLP and Transformers for insightful and context-aware interactions. <br/>
  It offers a user-friendly interface for querying document-specific information, streamlining access to key insights and information.</h3>
<br>

![Screenshot (271)](https://github.com/crazytrain328/DocuBot/assets/113792434/850f1456-805c-4108-a2b5-236bdeffe934)


<h2>To Run this Project </h2> 


1) Download This Repository.
   ```bash
   git clone https://github.com/crazytrain328/DocuBot.git
   ```
2) Install Virtual Environment for Python
   ```bash
   pip install virtualenv
   ```
3) Create New Virtual Environment.
   ```bash
   virtualenv env
   ```
4) Make sure you have Python and pip installed</br>
   To Install Python:
   ```bash
   https://realpython.com/installing-python/
   ```
   To install pip:
   ```bash
   python get-pip.py
   ```
5) Install Django
   ```bash
   pip install django
   ```
6) Create A New Django Project.
   ```bash
   django-admin startproject DocuBot.
   ```
7) Create a New App Base.
   ```bash
   django-admin startapp base
   ```
8) Delete all the created files inside main DocuBot directory and copy and paste the Files in This repository.
9) Copy the env folder inside main DocuBot folder.
10) Change the working directory to DocuBot
   ```bash
      cd DocuBot
   ```  
11) Activate the Virtual Environment.<br>
   i) Windows
      ```bash
         env\scripts\activate
      ```
   ii) Linux
      ```bash
         source env\bin\activate
  
12) Start the Server.
   ```bash
      python manage.py runserver
   ```
13) Go to the below URL to run the project.
    ```bash
    http://127.0.0.1:8000/
    ```  
