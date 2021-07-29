# create new user with home dir and bash as shell
sudo useradd -s /bin/bash -m user

# add user to group
sudo usermod -a -G group user

# remove user from group
sudo gpasswd -d user group

# change default shell to bash
chsh -s /bin/bash starfish

# add to sudoers
usermod -aG sudo starfish

# configure passwordless sudo
# https://linuxconfig.org/configure-sudo-without-password-on-ubuntu-20-04-focal-fossa-linux
# edit is %sudo ALL=(ALL:ALL) NOPASSWD:ALL