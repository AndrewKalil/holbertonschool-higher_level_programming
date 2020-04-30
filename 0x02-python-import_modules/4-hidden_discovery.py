#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list_names = dir(hidden_4)
    for i in range(len(list_names)):
        if (i[:2] == "__"):
            continue
        else:
            print(i)
