.PHONY: subtree-setup

subtree-setup:
	git subtree add --prefix external/talon_hud https://github.com/chaosparrot/talon_hud.git master --squash
	git subtree add --prefix external/rango https://github.com/david-tejada/rango-talon.git main --squash

.PHONY: subtree-pull
	git subtree pull --prefix external/talon_hud https://github.com/chaosparrot/talon_hud.git master --squash
	git subtree pull --prefix external/rango https://github.com/david-tejada/rango-talon.git main --squash



