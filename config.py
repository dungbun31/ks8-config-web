import os
from ruamel.yaml import YAML


def update_image_tag(file_path, new_tag):
    yaml = YAML()
    yaml.preserve_quotes = True

    with open(file_path, "r") as file:
        data = yaml.load(file)

    data["image"]["tag"] = new_tag

    with open(file_path, "w") as file:
        yaml.dump(data, file)


if __name__ == "__main__":
    file_path = "values.yaml"

    new_tag = os.getenv("NEW_TAG")

    if new_tag is None:
        print("Environment variable NEW_TAG is not set")
        exit(1)

    update_image_tag(file_path, new_tag)
