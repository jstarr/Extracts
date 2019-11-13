from datetime import datetime

while True:
    startTime = input('Start Time (\'HH:MM:SS\'):')
    if not startTime:
        break
    print(f'"{startTime}"')
    endTime = input('End Time (\'HH:MM:SS\'):')
    print(f'"{endTime}"')
    fmt = '%H:%M:%S'
    diff = datetime.strptime(endTime.lstrip(), fmt) - datetime.strptime(startTime.lstrip(), fmt)

    print(str(diff))
