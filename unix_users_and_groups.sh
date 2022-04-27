# create new user with home dir and bash as shell
sudo useradd -s /bin/bash -m <user>

# add user to group
sudo usermod -a -G <group> <user>

# remove user from group (yes, the command is gpasswd)
sudo gpasswd -d <user group>

# reset user's password
sudo passwd <user>

# change default shell to bash
chsh -s /bin/bash <user>

# add to sudoers
usermod -aG sudo <user>

# configure passwordless sudo
# https://linuxconfig.org/configure-sudo-without-password-on-ubuntu-20-04-focal-fossa-linux
# edit is %sudo ALL=(ALL:ALL) NOPASSWD:ALL