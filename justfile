datapack := "less-crafting"
multimc-world := "/home/rutrum/src/MultiMC/instances/dp_instance/.minecraft/saves/world/datapacks"

default: generate

generate:
		python3 generate.py

# Moves the pack to a multimc instance
test: generate
		rm -r {{multimc-world}}/{{datapack}}
		cp -r {{datapack}} {{multimc-world}}

clean:
		rm -r {{datapack}}

tree:
		tree -I {{datapack}}
