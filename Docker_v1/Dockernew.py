import os


def install():

	print('\nPlease make sure you have yum configured')

	z=1



	while z==1:
		ch = input('\nDo you want to continue?(y/n)\n')

		if str(ch) == 'y':
			print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Installing Docker , Please have patience++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

			
			
			os.system('''

			curl  https://download.docker.com/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo


			yum install docker-ce --nobest -y

			
			''')
			z=0
		elif str(ch) == 'n':
			print('\nOK , configure yum first\n')
			z=0	

		else:
			print('\nPress y or n\n')
	
	
	pull()
	new_cont()
	enter()


#pulling an image 


def pull():

	ch = input('want to pull an image?(y/n)\n')

	if str(ch) == 'y':
		nameos = input('Which os image would you like to install?\n')
		versionch = input('Do you want a specific version?(y/n)\n')
		if str(versionch) == 'y':
			version = input('which version?\n')
		else:
			version = 'latest'
		os.system('docker pull {}:{}'.format(nameos,version))
		print('\nImage downloaded\n')
	else:
		print("It's your choice \n")
		


#creating a container

def new_cont():

	inkk = input('Want to create a container?(y/n)\n')
	if str(inkk)== 'y':
		name = input('What name would you like to give to your container?\n')
		image = input('Which image would you like to use?\n')
		version_ch = input('Would you like to choose a specific version?(y/n)\n')
		if str(version_ch) == 'y':
			version = input('Which version?\n')
		else:
			version = 'latest'
			
		print('\nCreating a new container:{}'.format(name))
		os.system('docker run -dit --name {} {}:{}'.format(name,image,version))

	else:
		print('\nOk , we will create container later\n')


#Entering a container
def enter():

	enter_ch  = input('\nWould you like to enter a container?(y/n)\n')
	if str(enter_ch) == 'y':
		print('\nAvailable containers are:\n\n')
		os.system('docker ps -a ')
		
		container_ch = input('\nWhich container would you like to enter in?\n')
		os.system('docker start {}'.format(container_ch))
		os.system('docker attach {}'.format(container_ch))
	else:
		print('\nSee ya next time...........')


#Deleting a container
def delete():
	print('Available Containers are:\n')
	os.system('docker ps -a')
	os_name = input('\nWhich container would you like to Delete?')
	os.system('docker rm {}'.format(os_name))


#Stopping a container
def stop():
	print('Available Containers are:\n')
	os.system('docker ps -a')
	os_name = input('\nWhich container would you like to stop?')
	os.system('docker stop {}'.format(os_name))
	print('\b stopped')


#Available Containers

def show():
	os.system('docker ps -a')


#Configuring web server in container


def web():
	print('Make sure SElinux and firewall are disabled in base OS. You can disable them after installation but make sure to restart container\n')
	print('\nAvailable containers are:')
	os.system('docker ps -a')
	os_name = input('\nIn which container do you want to configure web server?\n')
	os.system("docker exec -it {} bash -c 'yum install httpd -y'".format(os_name))
	os.system('''docker exec {} bash -c "echo 'rm -rf /var/run/httpd/*  \n /usr/sbin/httpd' >> /root/.bashrc"'''.format(os_name))
	print('Successfully configured webserver in {}'.format(os_name))
	









	

