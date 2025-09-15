import os

def get_env_var(name):
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Environment variable {name} is not set")
    return value

aws_key = get_env_var("AWS_ACCESS_KEY_ID")
aws_secret = get_env_var("AWS_SECRET_ACCESS_KEY")
print(f"AWS Key: {aws_key}")
print(f"AWS Secret: {aws_secret}")

if __name__ == "__main__":
    get_env_var("AWS_ACCESS_KEY_ID")