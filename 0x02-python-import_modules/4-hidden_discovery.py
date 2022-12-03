#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    hide_list = dir(hidden)
    for lst in hide_list:
        if lst[0:2] != "__":
    	    print(lst)
