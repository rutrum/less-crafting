import os
import shutil

BUILD_DIR = "less-crafting"

def main():

    build_directory_structure()
    mv_pack_mcmeta()

    recipe_template = open("templates/shaped_crafting.json").read()
    adv_template = open("templates/shaped_crafting.json").read()

    with open("remove_list.txt") as f:
        for recipe in f:
            recipe = recipe.strip()

            recipe_filename = "{}/data/minecraft/recipes/{}.json".format(
                BUILD_DIR, recipe
            )

            with open(recipe_filename, "w") as out:
                out.write(recipe_template)

            adv_filename = "{}/data/minecraft/advancements/recipes/{}.json".format(
                BUILD_DIR, recipe
            )

            with open(adv_filename, "w") as out:
                out.write(adv_template)

def mv_pack_mcmeta():
    shutil.copyfile(
        "templates/pack.mcmeta",
        "{}/pack.mcmeta".format(BUILD_DIR)
    )

def build_directory_structure():
    os.makedirs("{}/data/minecraft/recipes".format(BUILD_DIR), exist_ok=True)
    os.makedirs("{}/data/minecraft/advancements/recipes".format(BUILD_DIR), exist_ok=True)

if __name__ == "__main__":
    main()
