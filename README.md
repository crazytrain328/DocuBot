# DocuBot
<h3>DocuBot is an innovative chatbot application designed to process and analyze content from uploaded PDF files, <br/>
  leveraging GPT-4 for insightful and context-aware interactions. <br/>
  It offers a user-friendly interface for querying document-specific information, streamlining access to key insights and information.</h3>
<br>


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
4) Create A New Django Project.
   ```bash
   django-admin startproject DocuBot.
   ```
5) Create a New App Base.
   ```bash
   django-admin startapp base
   ```
5) Delete all the created files inside studybudd and copy and paste the Files in This repository.
6) Copy the env folder inside studybudd folder.
7) Change the working directory to studybudd
   ```bash
      cd DocuBot
   ```  
8) Activate the Virtual Environment.<br>
   i) Windows
      ```bash
         env\scripts\activate
      ```
   ii) Linux
      ```bash
         source env\bin\activate
  
9) Start the Server.
   ```bash
      python manage.py runserver
   ```
10) Go to the below URL to run the project.
    ```bash
    http://127.0.0.1:8000/
    ```  
