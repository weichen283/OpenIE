import json
import os


def cut(str, num, x):
    return str[:num] + str[num + x:]


def main():
    path = input('Type folder path: ')
    files = os.listdir(path)

    for file in files:

        with open(path + '/' + file, 'r') as jsonfile:
            s = json.load(jsonfile)

        fh = open(file + '.txt', 'w')
        for i in range(len(s["body_text"])):
            string = s["body_text"][i]

            text = string["text"]
            start = []
            end = []

            for key in string["cite_spans"]:
                start.append(key["start"])
                end.append(key["end"])
            #print(start)
            #print(end)
            #print("-----------")
            for i in reversed(range(len(start))):

                if i!=0 and start[i]-end[i-1] ==1:
                    text = cut(text, start[i] - 1, end[i] - start[i] + 1)

                if i!=0 and start[i]-end[i-1] !=1:
                    text = cut(text, start[i] - 1, end[i] - start[i] + 2)

                if i==0:
                    text = cut(text, start[i] - 1, end[i] - start[i] + 2)



            fh.write(text)
            fh.write('\n')

        fh.close()


if __name__ == '__main__':
    main()
