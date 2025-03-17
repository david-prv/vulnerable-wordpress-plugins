import os
import subprocess
import argparse

DEPENDENCY_MAP: dict[str, str] = {
    "elementor": "elementor",
    "cf7": "contact-form-7",
    "woocommerce": "woocommerce",
    # "seo": "wordpress-seo",
    "acf": "advanced-custom-fields",
    "gutenberg": "gutenberg"
}

def run_wp_cli_command(command: str) -> bool:
    """ Function that runs a WP-CLI command and reports errors. """
    try:
        subprocess.run(command, check=True, text=True)
        return True
    except Exception as e:
        print(f"[!] Error while running command: {' '.join(command)}\n     => {e}")
        return False

def install_plugin(plugin_slug: str) -> bool:
    """ Auxiliary function that installs a plugin if confirmed. """
    print(f"[+] Installing plugin: {plugin_slug}")
    return run_wp_cli_command(["wp", "plugin", "install", plugin_slug, "--activate"])

def main(repository_path: str, skip_confirmation: bool, dump_results: bool) -> None:
    if not os.path.isdir(repository_path):
        print(f"[!] Error: {repository_path} is not a valid directory.")
        return

    installed_dependencies = set()
    failing_dependencies = set()

    for plugin_folder in os.listdir(repository_path):
        plugin_slug = plugin_folder.lower()

        for keyword, dependency in DEPENDENCY_MAP.items():
            if keyword in plugin_slug and keyword != plugin_slug and dependency not in installed_dependencies:
                print(f"[+] Detected dependency for {plugin_folder}: {dependency}")

                if not skip_confirmation:
                    confirmation = input("[+] Do you want to proceed? (Y/n) ")
                    if confirmation.lower() != "y" and confirmation.lower() != "yes":
                        continue

                if not dump_results:
                    if install_plugin(dependency):
                        installed_dependencies.add(dependency)
                        continue
                else:
                    print("     => Skipping automatic installation. Please install manually.")
                    installed_dependencies.add(dependency)
                    continue

                failing_dependencies.add(dependency)

    print(f"[+] Finished. {len(failing_dependencies)} errors occurred.")

    if dump_results and len(installed_dependencies) > 0:
        print("[!] The following dependencies need to be installed manually:")
        print(installed_dependencies)

    if len(failing_dependencies) > 0:
        print("[!] The following dependencies caused an error:")
        print(failing_dependencies)
    
    exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Install plugin dependencies for CVWP.")
    parser.add_argument(
        "repository_path",
        nargs="?",
        default="./",
        type=str,
        help="path to the repository containing vulnerable plugins."
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        default=False,
        help="skip manual user confirmation per plugin."
    )
    parser.add_argument(
        "-d",
        "--dump",
        action="store_true",
        default=False,
        help="skip automatic installation, just dump dependencies to terminal."
    )

    args = parser.parse_args()

    main(
        os.path.abspath(args.repository_path),
        bool(args.yes),
        bool(args.dump)
    )
