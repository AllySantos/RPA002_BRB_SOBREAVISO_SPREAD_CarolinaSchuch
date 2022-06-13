import os

# Get windows logged username
windows_username = os.environ.get('USERNAME')

# Concat to make the bot folder path
bot_folder_path = f'C:\\Users\\{windows_username}\\BotSobreaviso'

# Return it to ElectroNeek
print(bot_folder_path)
