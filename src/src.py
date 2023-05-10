import os
import glob
import pprint

def get_resources():
    resource_dict = {}
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    terraform_dir = os.path.join(parent_dir, "terraform")
    pp = pprint.PrettyPrinter(indent=8)
    tf_files = glob.glob(os.path.join(terraform_dir, "*.tf"))

    for tf_file in tf_files:
        filename = os.path.basename(tf_file)
        with open(tf_file, "r") as f:
            content = f.read()

        resources = []
        lines = content.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("resource"):
                resource_type = line.split(" ")[1].replace('"', "")
                resource = line.split(" ")[2].replace('"', "")
                resource_name = resource.split(".", 1)
                resources.append(f"{resource_type}: {resource_name}")

        filename = os.path.basename(tf_file)
        resource_dict[filename] = resources
    print({"filename: [resources_type: ['resource_name']"})
    print("\n")
    for filename, resources in resource_dict.items():
        pp.pprint(f"{filename}: {resources}\n")

get_resources()
