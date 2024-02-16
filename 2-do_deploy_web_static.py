#!/usr/bin/python3
#fabric projects for ssh
from fabric.api import env, put, run
from os.path import exists

# Define the server IPs or hostnames
env.hosts = ['54.227.179.101', '3.90.204.71']
# Set the user and optionally the SSH key if needed
env.user = 'ubuntu'
# env.key_filename = '/Users/alana/.ssh/id_rsa'

def do_deploy(archive_path):
    # Check if the archive_path exists
    if not exists(archive_path):
        print("The file at the path {} doesn’t exist".format(archive_path))
        return False

    try:
        # Extract the file name and the name without extension
        file_name = archive_path.split("/")[-1]
        name_without_extension = file_name.split(".")[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/{}'.format(file_name))

        # Uncompress the archive to the folder on the web server and remove the archive
        target_path = '/data/web_static/releases/{}'.format(name_without_extension)
        run('mkdir -p {}'.format(target_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, target_path))
        run('rm /tmp/{}'.format(file_name))

        # Delete the symbolic link and create a new one
        run('rm -f /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(target_path))

        print("Deployment done successfully.")
        return True
    except:
        print("Deployment failed.")
        return False

