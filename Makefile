install:
	sudo cp moon.service /etc/systemd/system/
	sudo systemctl enable moon.service
	sudo systemctl start moon.service

uninstall:
	sudo systemctl stop moon.service
	sudo systemctl disable moon.service
	sudo rm /etc/systemd/system/moon.service

listen:
	sudo journalctl -f -u moon.service
reload:
	sudo systemctl daemon-reload

.PHONY: install uninstall


