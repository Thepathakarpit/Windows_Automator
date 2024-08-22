import google.generativeai as genai
import os
from subprocess import Popen

#Enter your api key between the quotes below, which you can get at https://aistudio.google.com/app/apikey
api = " " 

if(api==" "):
  api = input("Please input your gemini api key: ")
genai.configure(api_key=api)

model = genai.GenerativeModel('gemini-1.5-flash')
def main():
  ques = input("Please enter your prompt: ")
  #Pro tip: You can do anything at cmd using bat file so use your imagination and problemsolving you can do almost everything. wink wink! You can create and run files including code files like py, install and use libraries, think... 

  #Prompt is set to generate a batch file for the given task but you can modify it accordingly if you want.
  response = model.generate_content("Generate batch file to automate the task I am about to tell you. Don't output any additional symbols or any comments straight up executable batch file.:Please Generate a batch file that"+ques)

  if os.path.exists("file.txt"):
    os.remove("file.txt")

  if os.path.exists("file.bat"):
    os.remove("file.bat")
  f = open("file.bat", "x")
  f = open("file.bat", "a")
  f.write(response.text)
  f.close()

  path = os.getcwd()
  p = Popen("file.bat", cwd=path)
  stdout, stderr = p.communicate()
while(1):
  main()
