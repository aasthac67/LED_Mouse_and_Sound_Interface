import speech_recognition as sr
import os

def lastword(text):
	x = text.strip()

	s=""
	for i in range(len(x)):
		if x[i]==" ":
			s=""
		else:
			s+=x[i]
	return s

def main():
	print("-------- Controlling the terminal with Speech ---------")
	r = sr.Recognizer()

	with sr.Microphone() as source:
		while(1):

			print("")
			print("Which command do you want to implement? ")
			print("")
			print("List of commands: ")
			print("1) create directory")
			print("2) make python file")

			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			text = r.recognize_google(audio)
			print("I heard ",text)

			if(str(text).find("create directory")):
				dir_name = lastword(text)
				cmd = 'mkdir '+dir_name
				os.system(cmd)

			if(str(text).find("make python file")):
				file_name = lastword(text)
				cmd = 'touch '+file_name+'.py'
				os.system(cmd)


if __name__ =="__main__":
	main()