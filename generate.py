import os
import shutil

BUILD_DIR = "less-crafting"

def main():
    recipe_template = open("templates/shaped_crafting.json").read()
    adv_template = open("templates/advancement.json").read()

    recipes = [ recipe.strip() for recipe in open("remove_list.txt") ]
    advancement_path, adv_categories = get_recipe_to_adv_path(recipes)

    build_directory_structure(adv_categories)
    mv_pack_mcmeta()

    for recipe in recipes:
        recipe_filename = "{}/data/minecraft/recipes/{}.json".format(
            BUILD_DIR, recipe
        )

        with open(recipe_filename, "w") as out:
            out.write(recipe_template)

        # recipes are in subdirectories.  Need to find them first by name
        if recipe in advancement_path:
            adv_path = advancement_path[recipe]
            adv_filename = f"{BUILD_DIR}/data/minecraft/advancements/{adv_path}"

            with open(adv_filename, "w") as out:
                out.write(adv_template)

def mv_pack_mcmeta():
    shutil.copyfile(
        "templates/pack.mcmeta",
        "{}/pack.mcmeta".format(BUILD_DIR)
    )

def get_recipe_to_adv_path(recipes):
    """ Creates a map that maps a filename to its advancement location """
    start_path = "minecraft_datapack/advancements"
    d = {}
    adv_categories = set()
    for root, dirs, files in os.walk(start_path):
        for file in files:
            stem = file.split(".")[0]
            for recipe in recipes:
                if stem == recipe:
                    root_path = "/".join(root.split("/")[2:])
                    d[recipe] = f"{root_path}/{file}"
                    category = root_path.split("/")[1] # recipes/building_blocks/andesite_slab.json
                    adv_categories.add(category)
    return d, adv_categories

def build_directory_structure(categories):
    os.makedirs(f"{BUILD_DIR}/data/minecraft/recipes", exist_ok=True)
    os.makedirs(f"{BUILD_DIR}/data/minecraft/advancements/recipes", exist_ok=True)
    for cat in categories:
        os.makedirs(f"{BUILD_DIR}/data/minecraft/advancements/recipes/{cat}", exist_ok=True)

if __name__ == "__main__":
    main()
