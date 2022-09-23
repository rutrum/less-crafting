datapack := "less-crafting"
multimc-world := "~/.local/share/PolyMC/instances/less-crafting/.minecraft/saves/New\\ World/datapacks"

default: generate

generate:
    python3 generate.py

# Moves the pack to a multimc instance
test: generate
    -rm -r {{multimc-world}}/{{datapack}}
    cp -r {{datapack}} {{multimc-world}}

clean:
    rm -r {{datapack}}

tree:
    tree -I {{datapack}}
