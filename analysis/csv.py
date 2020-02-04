import os
import logging as lg

lg.basicConfig(level=lg.DEBUG)

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)

    try:
        with open(path_to_file, 'r') as file:
            preview = file.readline() #read first line
        lg.debug("Yea! We managed to read the file. Here is a preview: {}".format(preview))
    except IOError as e:
        lg.critical('Ow :( The file was not found. Here is the message: {}'.format(e))

    

def main():
    launch_analysis('current_mps.csv')
    

if __name__ == "__main__":
    main()