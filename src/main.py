import os
from androguard.core.apk import APK

def extract_permissions(apk_path, output_option):
    try:
        # Expand the tilde in case user enters '~' as shorthand for the home directory
        apk_path = os.path.expanduser(apk_path)
        print(f"Analyzing APK at path: {apk_path}")

        # Load the APK file using Androguard's APK class
        # This class automatically handles parsing and decoding of AndroidManifest.xml
        apk = APK(apk_path)

        # Extract permissions declared in the APK's AndroidManifest.xml
        permissions = apk.get_permissions()

        # Validate the presence of permissions in the APK
        if not permissions:
            print("No permissions found in the APK.")
            return

        print(f"Retrieved permissions: {permissions}")

        # Format the output for better readability
        header = f"Permissions for {apk_path}:\n"
        formatted_permissions = "\n".join(f"- {perm}" for perm in permissions)
        result = header + formatted_permissions

        # Handle output based on the user's choice (screen or file)
        if output_option == "file":
            output_file = input("Enter a filename (e.g., 'permissions.txt'): ").strip()
            with open(output_file, "w") as f:
                f.write(result + "\n")
            print(f"\nPermissions successfully written to '{output_file}'.")
        else:
            print("\n" + result)

    except Exception as e:
        # Handle any unexpected errors gracefully and print the error message
        print(f"Error analyzing {apk_path}: {e}")

if __name__ == "__main__":
    # Prompt the user for the APK file path and output option
    apk_path = input("Enter the path to the APK file: ").strip()
    output_option = input("Print to 'screen' or 'file'?: ").strip().lower()

    # Call the permission extraction function with the provided inputs
    extract_permissions(apk_path, output_option)
