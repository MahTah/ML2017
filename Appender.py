import pandas as pd
import time
import os

def Appender(full_dataframe, merge_data, input_folder):
    df1 = full_dataframe
    df2 = pd.read_csv(input_folder+'/' + merge_data)

    # Append
    df = df1.append(df2)

    # Save
    # df.to_csv(output_name, index=None)
    return df


if __name__ == "__main__":
    start = time.time()

    # Initialize dataframe
    full_df = pd.DataFrame()
    # # need to check that the two dataset are the same month
    # full_df = Appender(full_dataframe = full_df, merge_data="clean_2016-01-merged.csv", \
    #       input_folder="./data/merged")
    # full_df = Appender(full_dataframe=full_df, merge_data="clean_2016-02-merged.csv", \
    #                    input_folder="./data/merged")
    # print "append time:"
    # print time.time() - start

    inputFolder = "./data"
    for test in os.listdir(inputFolder):
        if "merged" in test and ".zip" not in test:
            for filename in os.listdir(inputFolder + "/" + test):
                if "merged" in filename:
                    start = time.time()
                    full_df = Appender(full_dataframe = full_df, merge_data=filename, \
                                       input_folder=inputFolder + "/" + test)

                    print "Appending time:"
                    print time.time() - start

    full_df.to_csv(inputFolder+"/appended/2016_clean.csv", index=None)