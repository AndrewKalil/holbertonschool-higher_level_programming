#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list_names = dir(hidden_4)
    for i in range(len(list_names)):
        if (list_names[i][0] != "_" and list_names[i][1] != "_"):
            print(list_names[i])
