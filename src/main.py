import os
from androguard.misc import AnalyzeAPK

def analyze_permissions(apk_path, output_option):
    try:
        # Expand the tilde in case user enters '~' in the path as home directory
        apk_path = os.path.expanduser(apk_path)
        
        # Analyze the APK file and extract permissions
        a, d, dx = AnalyzeAPK(apk_path)
        permissions = a.get_permissions()

        # Format the output
        header = f"Permissions for {apk_path}:\n"
        formatted_permissions = "\n".join(f"- {perm}" for perm in permissions)
        result = header + formatted_permissions

        if output_option == "file":
            # Ask for a filename and write the result to that file
            output_file = input("Enter a filename (e.g., 'permissions.txt'): ")
            with open(output_file, "w") as f:
                f.write(result + "\n")
            print(f"\nPermissions successfully written to '{output_file}'.")
        else:
            # Print the result to the screen
            print("\n" + result)

    except Exception as e:
        print(f"Error analyzing {apk_path}: {e}")

if __name__ == "__main__":
    apk_path = input("Enter the path to the APK file: ")
    output_option = input("Print to 'screen' or 'file'?: ").strip().lower()
    analyze_permissions(apk_path, output_option)
