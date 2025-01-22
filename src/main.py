import os
from datetime import datetime
from androguard.core.apk import APK

# List of Android dangerous permissions
DANGEROUS_PERMISSIONS = {
    "android.permission.READ_CALENDAR",
    "android.permission.WRITE_CALENDAR",
    "android.permission.CAMERA",
    "android.permission.READ_CONTACTS",
    "android.permission.WRITE_CONTACTS",
    "android.permission.GET_ACCOUNTS",
    "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.ACCESS_COARSE_LOCATION",
    "android.permission.RECORD_AUDIO",
    "android.permission.READ_PHONE_STATE",
    "android.permission.CALL_PHONE",
    "android.permission.READ_CALL_LOG",
    "android.permission.WRITE_CALL_LOG",
    "android.permission.ADD_VOICEMAIL",
    "android.permission.USE_SIP",
    "android.permission.PROCESS_OUTGOING_CALLS",
    "android.permission.BODY_SENSORS",
    "android.permission.SEND_SMS",
    "android.permission.RECEIVE_SMS",
    "android.permission.READ_SMS",
    "android.permission.RECEIVE_WAP_PUSH",
    "android.permission.RECEIVE_MMS",
    "android.permission.READ_EXTERNAL_STORAGE",
    "android.permission.WRITE_EXTERNAL_STORAGE"
}

def extract_permissions(apk_path, output_option):
    try:
        # Expand user shortcuts in the APK path
        apk_path = os.path.expanduser(apk_path)
        print(f"Analyzing APK at path: {apk_path}")

        # Load the APK file
        apk = APK(apk_path)
        permissions = apk.get_permissions()

        if not permissions:
            print("No permissions found in the APK.")
            return

        # Sort permissions alphabetically
        permissions = sorted(permissions)

        # Separate permissions into dangerous and other categories
        dangerous_permissions = [perm for perm in permissions if perm in DANGEROUS_PERMISSIONS]
        other_permissions = [perm for perm in permissions if perm not in DANGEROUS_PERMISSIONS]

        # Gather metadata
        app_name = apk.get_app_name() or "Unknown"
        package_name = apk.get_package() or "Unknown"
        version_name = apk.get_androidversion_name() or "Unknown"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format headers and summaries
        header = f"========= Permissions Analysis =========\n"
        metadata = (
            f"File: {apk_path}\n"
            f"App Name: {app_name}\n"
            f"Package Name: {package_name}\n"
            f"Version: {version_name}\n"
            f"Analysis Date: {timestamp}\n"
            f"========================================\n"
        )
        summary = (
            f"Summary:\n"
            f"- Total permissions: {len(permissions)}\n"
            f"- Dangerous permissions: {len(dangerous_permissions)}\n"
            f"- Other permissions: {len(other_permissions)}\n\n"
        )

        # Format permissions lists
        dangerous_header = "Dangerous Permissions:\n"
        formatted_dangerous = "\n".join(f"- {perm}" for perm in dangerous_permissions)
        other_header = "\nOther Permissions:\n"
        formatted_other = "\n".join(f"- {perm}" for perm in other_permissions)

        # Combine all output into a single string
        result = (
            header + metadata + summary +
            dangerous_header + formatted_dangerous + "\n" +
            other_header + formatted_other + "\n"
        )

        # Handle output based on user choice
        if output_option == "file":
            # Automatically generate a filename
            apk_name = os.path.basename(apk_path).replace(".apk", "")
            output_file = f"permissions_{apk_name}_{datetime.now().strftime('%Y%m%d')}.txt"
            with open(output_file, "w") as f:
                f.write(result)
            print(f"\nPermissions successfully written to '{output_file}'.")
        else:
            # Print permissions to the screen
            print("\n" + result)

    except Exception as e:
        # Handle any errors during processing
        print(f"Error analyzing {apk_path}: {e}")

if __name__ == "__main__":
    # Prompt user for the APK path and output method
    apk_path = input("Enter the path to the APK file: ").strip()
    output_option = input("Print to 'screen' or 'file'?: ").strip().lower()
    extract_permissions(apk_path, output_option)
