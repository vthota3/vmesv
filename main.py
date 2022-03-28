##
# Main.py 
# Description:

#
# RM_PROD : Needs to be removed during deployment

# imports
import argparse
import yaml

class main:
    
    def __init__(self):
        #RM_PROD print("In the INIT method")
        self.get_variables()


    def yaml_loader(self,filepath):
        with open(filepath,"r") as file_descriptor:
            data = yaml.safe_load(file_descriptor)
        print(data)
        return data


    def get_variables(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--file',type=str,required=True)
        args = parser.parse_args()
        print("File Provided by user: "+args.file)
        self.yaml_loader(args.file)

    def print_obj(self):
        print("Main Object") 


if __name__ == '__main__':
    main_obj = main()
    main_obj.print_obj()



