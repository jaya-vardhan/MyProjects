file_data = open("./vim_notes.txt").readlines()

for line in file_data:
	if "NOTE" in line:
		with open("test", 'a+') as write_file:
			write_file.write(line)

