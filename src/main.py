from androguard.misc import AnalyzeAPK

def analyze_permissions(apk_path):
    try:
        # Analyze the APK file and extract permissions
        a, d, dx = AnalyzeAPK(apk_path)
        permissions = a.get_permissions()
        print(f"Permissions for {apk_path}:")
        for permission in permissions:
            print(f"- {permission}")
    except Exception as e:
        print(f"Error analyzing {apk_path}: {e}")

if __name__ == "__main__":
    apk_path = input("Enter the path to the APK file: ")
    analyze_permissions(apk_path)

