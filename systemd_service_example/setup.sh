sudo cp run_shuttlepro.sh /opt/shuttlepro
sudo cp ./shuttlepro.service /etc/systemd/system
sudo systemctl start shuttlepro.service