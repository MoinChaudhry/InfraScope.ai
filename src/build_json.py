import hcl2
import json
import os
import glob


def build_json():
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    terraform_dir = os.path.join(parent_dir, "terraform")
    tf_files = glob.glob(os.path.join(terraform_dir, "*.tf"))
    print(tf_files)
    if not tf_files:
        print("No Terraform files found in the specified directory.")
        return
    json_resources = []
    for tf_file in tf_files:
        print(tf_file)
        with open(tf_file, "r") as f:
            try:
                terraform_code = f.read()
                hcl_parser = hcl2.loads(terraform_code)
                for resource in hcl_parser["resource"]:
                    json_resources.append(resource)
            except Exception as e:
                print(f"Error processing {tf_file}: {str(e)}")
    if json_resources:
        output_file = os.path.join(terraform_dir, "resources.json")
        with open(output_file, "w") as f:
            json.dump(json_resources, f, indent=4)
        print(f"JSON resources written to {output_file}")
    else:
        print("No Terraform resources found.")
if __name__ == '__main__':
    build_json()
