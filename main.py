import subprocess


def update_packages():
    try:
        subprocess.run(['pip', 'install', '--upgrade', 'pip'], check=True)

        outdated_packages = subprocess.check_output(['pip', 'list', '--outdated']).decode('utf-8').split('\n')[2:]

        for package_info in outdated_packages:
            if package_info:
                package_name = package_info.split()[0]
                subprocess.run(['pip', 'install', '--upgrade', '--no-cache-dir', package_name], check=True)

        print("Software update completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("Software update failed.")


if __name__ == "__main__":
    update_packages()
