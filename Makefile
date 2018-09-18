
SCRIPT_DIR=$$(pwd)/scripts

.PHONY: all
all: setup provision


.PHONY: setup
setup: check.xcode
	@$(SCRIPT_DIR)/InstallAnsible.sh
	@$(SCRIPT_DIR)/UpdateAnsible.sh

.PHONY: provision
provision: check.xcode
	python $(SCRIPT_DIR)/play_ansible.py
	@$(SCRIPT_DIR)/NotifyFinished.sh

.PHONY: check.xcode
check.xcode:
	@$(SCRIPT_DIR)/CheckXcode.sh
