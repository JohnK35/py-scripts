import getopt, sys
import pandas as pd

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:v", ["help", "inputfile"])
    except getopt.GetoptError as err
        print(err)
        sys.exit(2)
    input = None
    for o, a in opts:
        if o in ("-i", "--input"):
            input = a
            operations(input)
        elif o in ("-h", "--help"):
            print("Usage: python acsfilter.py [OPTION] [FILE] ...")
            print("Example: python csvfilter.py -i filename.csv")
            sys.exit()
        else:
            sys.exit()

def operations(inputfile):
    df = pd.read_csv(inputfile)
    col_name = ['DateStart','Name','LastName','Status','Position','Department'] #for create columns name
    empposition = ['Officer','Senior Officer','Assistant Manager','Manager'] #for filter each position
    savename = ['emp_officer.csv', 'emp_senior_officer.csv', 'assistant_manager.csv', 'manager.csv']  #for save file
    col = [0, 1, 2, 7, 8] # unuse number of column
    datafilter = df.drop(df.columns[[col]], axis=1)  # for delete unuse column follow number of column
    datafilter.columns = col_name  # make colums name
    for i, n in zip(empposition, savename) : # filter csv file with position and save
        realdata = datafilter.loc[datafilter['Position'] == i]
        realdata.to_csv(n, index=None, header=True)
        print("Save to " + n)
    print("Completed!!")

if __name__ == "__main__":
    main()