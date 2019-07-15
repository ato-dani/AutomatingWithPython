#!usr/bin/python3.6
#This is a python script that renames files with American-Style Dates to European-Style Dates and also the reverse
import re,os,shutil,logging,time

logging.basicConfig(level = logging.DEBUG, format="%(asctime)s - %(levelname)s -%(message)s")
def reg_ex_finder(file_name):
    pattern = re.compile("(.*)(\d\d-\d\d-\d\d\d\d)(.*)")
    return pattern.findall(file_name)
def rename_files(given_path):
    if not os.path.exists(given_path):
        print("The given path does not exist.")
    elif os.path.isfile(given_path):
            print("Searched 1 File ", end="")
            cur_file = reg_ex_finder(given_path)
            if len(cur_file) > 0:
                splitted_files = cur_file[0][1].split("-")
                shutil.move(this_file, cur_file[0][0] + splitted_files[1] + "-" + splitted_files[0] + "-" + splitted_files[2] + cur_file[0][2])
                print("Changed 1 File. ")
            else:
                print("Changed 0 File. ")
    else:
        searched_number = 0
        changed_number = 0
        for folder, subdirectories, files in os.walk(given_path):
            for this_file in files:
                searched_number += 1
                cur_file = reg_ex_finder(this_file)
                if len(cur_file) > 0:
                    splitted_files = cur_file[0][1].split("-")
                    renamed_file =  cur_file[0][0] + splitted_files[1] + "-"+ splitted_files[0] + "-"+ splitted_files[2] + cur_file[0][2]
                    shutil.move(this_file, renamed_file)
                    changed_number += 1
                time.sleep(1)
                print("\rSearched %d file(s) and changed %d file(s)" % (searched_number, changed_number), end="")
def main():
    given_path = input("Please enter the path of the directory to be searched for (e.g enter \".\" for the current directory and its sub directories): ")
    logging.info("Type of given_path: " + str(type(given_path)))
    logging.info("The given Path: " + given_path)
    logging.info("is the given path a directory? " + str(os.path.isdir(given_path)))
    rename_files(given_path)

if __name__ == "__main__":
    main()


