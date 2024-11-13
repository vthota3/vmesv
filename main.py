##
# Main.py 
# Description:

#
# RM_PROD : Needs to be removed during deployment

# imports
import argparse
import yaml

class main:
    ## Function Name: __init__
    ## Description: constructor function
    def __init__(self):
        #RM_PROD print("In the INIT method")
        self.get_args()

    ## Function Name: yaml_loader
    ## Description: This function is used to convert the input yaml file into dictoniary 
    def yaml_loader(self,filepath):
        with open(filepath,"r") as file_descriptor:
            data = yaml.safe_load(file_descriptor)
        print(data)
        return data

    ## Function Name: get_args
    ## Description: This function is used to get parse the args
    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--file',type=str,required=True)
        args = parser.parse_args()
        print("File Provided by user: VPT "+args.file)
        self.yaml_loader(args.file)



if __name__ == '__main__':
    main_obj = main()



