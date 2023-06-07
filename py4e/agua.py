import re
def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()

    # YOUR CODE HERE
    pattern="""(?P<host>[0-9.]+)( - )(?P<user_name>\S+)(\s\S)(?P<time>.+)(] ")(?P<request>.+)" [0-9]*"""
    lst=list()
    for item in re.finditer(pattern,logdata):
        lst.append(item.groupdict())
    return lst
    raise NotImplementedError()


print(len(logs()))