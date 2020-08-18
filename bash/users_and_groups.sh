# create new user with home dir and bash as shell
sudo useradd -s /bin/bash -m user

# add user to group
sudo usermod -d -G group user

# remove user from group
sudo gpasswd -d user group