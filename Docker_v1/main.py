import Dockernew
import os

while True:
	os.system('clear')
	print('===========================Welcome to Docker===================================')

	print('''

	1. Install Docker.
	2. Pull an Image.
	3. Create a container
	4. Enter a container
	5. Stop a container
	6. Delete a container
	7. Available Containers
	8. Available Images
	9. Configure webserver in a container
	10. Exit from the menu


	''')

	ch = input('What do you want to do?\n')

	if int(ch) == 1:
		Dockernew.install()
	elif int(ch) == 2:
		Dockernew.pull()
	elif int(ch) == 3:
		Dockernew.new_cont()
	elif int(ch) == 4:
		Dockernew.enter()
	elif int(ch) == 6:
		Dockernew.delete()
	elif int(ch)==5:
		Dockernew.stop()
	elif int(ch) == 7:
		Dockernew.show()
	elif int(ch) == 8:
		os.system('docker images')
	elif int(ch) == 9:
		Dockernew.web()
	elif int(ch) == 10:
		break
		os.system('exit')
	else:
		print('Invalid option')
	input('\n\n\nenter to continue')
		
