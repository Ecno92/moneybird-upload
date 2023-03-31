.PHONY: link
link:
	ln -s $(PWD)/moneybird_upload.py ~/.local/share/nautilus/scripts/moneybird_upload

.PHONY: settings
settings:
	@bash -c 'read -p "Enter the API token: " && echo $$REPLY > settings'
	@bash -c 'read -p "Enter the administration ID: " && echo $$REPLY >> settings'

