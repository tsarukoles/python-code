# Task_208

file_size = int(input("Enter the file size in GB:"))
internet_speed = int(input("Enter the internet speed:"))
file_size_bits = file_size*8*1024**3
download_time_seconds = file_size_bits/internet_speed
print("1.Downloading time - Hour:\n2. Downloading time - Minutes:\n3. Downloading time - Seconds:")
estimate_time = int(input("Please, enter Downloading time option:"))
if estimate_time == 1:
    print(int(download_time_seconds / 3600))
elif estimate_time == 2:
    print(int(download_time_seconds / 60))
elif estimate_time == 3:
    print(int(download_time_seconds))
else:
    print("Invalid data")