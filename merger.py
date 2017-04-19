import pandas as pd
import time
import os

def Merge(full_data, story_data , input_folder, output_name):
    df1 = pd.read_csv(input_folder+'/' + full_data)
    df2 = pd.read_csv(input_folder+'/' + story_data)

    # Merge
    df = pd.merge(df1, df2, how='inner', on=['RP_STORY_ID','TIMESTAMP_UTC'])

    # Drop two nonsense columns
    df.drop(['RP_STORY_ID','PROVIDER_ID'], inplace=True, axis=1)

    # Save
    df.to_csv(output_name, index=None)
    print df.columns


if __name__ == "__main__":
    start = time.time()

    # # need to check that the two dataset are the same month
    # Merge(full_data= "2016-01-equities_clean.csv", story_data="2016-01-storydata_clean.csv", \
    #       input_folder="~/PycharmProjects/rvpk", output_name="2016-01_merged.csv")
    # print "merge time:"
    # print time.time() - start

    inputFolder = "./data"
    for test in os.listdir(inputFolder):
        if "clean" in test and ".zip" not in test:
            for filename in os.listdir(inputFolder + "/" + test):
                if "equities" in filename:
                    start = time.time()
                    Merge(full_data = filename, story_data = filename.replace("equities", "storydata"), \
                          input_folder=inputFolder + "/" + test, \
                          output_name="data/merged/" + filename.replace("equities","merged"))
                    print "Merging time:"
                    print time.time() - start


