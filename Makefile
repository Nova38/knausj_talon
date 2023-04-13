.PHONY: subtree-setup

subtree-setup:
	git subtree add --prefix external/talon_hud https://github.com/chaosparrot/talon_hud.git master --squash
