
data_dict = {"india": "delhi", "france": "paris","uk": "london", "usa": "washington"}
with open("file/a.txt", "w") as fw:
    for country, captail in data_dict.items() :
        fw.write("the captail of {} is {}\n".format(country, captail))

with open("file/a.txt", encoding="utf8") as fd:
    for line in fd :
        print(line)

        