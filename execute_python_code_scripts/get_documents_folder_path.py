import os

# Get windows logged username
windows_username = os.environ.get('USERNAME')

# Concat to make the download folder path
download_path = f'C:\\Users\\{windows_username}\\Documents'

# Return it to ElectroNeek
print(download_path)
