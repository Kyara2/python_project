

import os
from os import system 
def main():
	file_source = input("Type the name of the file txt: ")
	file_name = open(file_source+".txt","r", encoding="UTF-8")
	lines = file_name.readlines()
	file_name.close()

	emails = []
	for line in lines:
		position_start = line.find("E-mail: ")
		position_end = line.find("	Enviar Mensagem")

		if position_start !=-1:
			email_begin = position_start+8

			if position_end != -1:
				email_end = position_end

				email_address = line[email_begin : email_end]

				email_address +=",\n"
				emails.append(email_address)


	#print(emails)

	target_file = open("alunos.txt","w")
	for email in emails:
		target_file.write(email)
	target_file.close()


	print("emails salvos no arquivo alunos.txt")

	system("subl alunos.txt")



if __name__ == "__main__":
	main()
