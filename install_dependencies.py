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

def run_wp_cli_command(command: str) -> None:
    """ Function that runs a WP-CLI command and reports errors. """
    try:
        subprocess.run(command, check=True, text=True)
    except Exception as e:
        print(f"[!] Error while running command: {' '.join(command)}\n     => {e}")

def install_plugin(plugin_slug: str) -> None:
    """ Auxiliary function that installs a plugin if confirmed. """
    print(f"[+] Installing plugin: {plugin_slug}")
    run_wp_cli_command(["wp", "plugin", "install", plugin_slug, "--activate"])

def main(repository_path: str, skip_confirmation: bool) -> None:
    if not os.path.isdir(repository_path):
        print(f"[!] Error: {repository_path} is not a valid directory.")
        return

    installed_dependencies = set()

    for plugin_folder in os.listdir(repository_path):
        plugin_slug = plugin_folder.lower()

        for keyword, dependency in DEPENDENCY_MAP.items():
            if keyword in plugin_slug and dependency not in installed_dependencies:
                print(f"[+] Detected dependency for {plugin_folder}: {dependency}")

                if not skip_confirmation:
                    confirmation = input("[+] Do you want to proceed? (Y/n) ")
                    if confirmation.lower() != "y" and confirmation.lower() != "yes":
                        continue

                install_plugin(dependency)
                installed_dependencies.add(dependency)

    print("[+] Finished.")

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

    args = parser.parse_args()

    main(
        os.path.abspath(args.repository_path),
        bool(args.yes)
    )
