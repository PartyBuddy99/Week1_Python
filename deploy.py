import sys

def deploy_message(name, environment):
    return f"Deploying the {name} in the {environment}"

if __name__ == "__main__":
    name = sys.argv[1],
environment = sys.argv[2],
print(deploy_message(name, environment))