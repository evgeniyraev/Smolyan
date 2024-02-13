install:
	sudo cp /asound.conf /etc/asound.conf
	sudo cp moon.service /etc/systemd/system/
	sudo systemctl daemon-reload
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
	sudo systemctl stop moon.service
	sudo systemctl start moon.service

.PHONY: install uninstall


