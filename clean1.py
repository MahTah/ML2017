import pandas as pd
import time
import os

def Clean_Equity(input_name, input_folder, output_name, extracols = [] ):
    # clean full data

    filename = input_folder+'/'+input_name
    usecols =  [u'TIMESTAMP_UTC',] + [u'RP_STORY_ID', u'ESS', u'CSS',u'RP_ENTITY_ID', u'ENTITY_TYPE', u'ENTITY_NAME'] + extracols
    df = pd.read_csv(filename, usecols = usecols)


    # Only keep records that have ESS score
    df = df.dropna(subset = [u'ESS',])
    df.to_csv(output_name, index = None)




def Clean_Story(input_name, input_folder, output_name, extracols = []):
    # clean story data

    filename = input_folder+'/'+input_name
    usecols =  [u'TIMESTAMP_UTC',] + [u'RP_STORY_ID', u'PROVIDER_ID', u'HEADLINE'] + extracols
    df = pd.read_csv(filename, usecols = usecols)

    # Only keep records that has provider Dow Jones
    df = df.loc[df[u'PROVIDER_ID'] == 'DJ']

    df.to_csv(output_name, index = None)


if __name__ == "__main__":

    # start = time.time()
    # Clean_Equity(input_name = "2016-01-equities.csv", input_folder = "~/PycharmProjects/rvpk", \
    #                   output_name = "2016-01-equities_clean.csv")
    # print "equity cleaning time:"
    # print time.time() - start
    #
    # start = time.time()
    # Clean_Story(input_name = "2016-01-storydata.csv", input_folder="~/PycharmProjects/rvpk", \
    #                 output_name = "2016-01-storydata_clean.csv")
    # print "story cleaning time:"
    # print time.time() - start

    # inputFolder = "./data"
    # for test in os.listdir(inputFolder):
    #     if "Equities" in test and ".zip" not in test:
    #         for filename in os.listdir(inputFolder+"/"+test):
    #             start = time.time()
    #             Clean_Equity(input_name = filename, input_folder = inputFolder+"/"+test, \
    #                         output_name = "data/clean/clean_"+filename)
    #             print "equity cleaning time:"
    #             print time.time() - start


    inputFolder = "./data"
    for test in os.listdir(inputFolder):
        if "story" in test and ".zip" not in test:
            for filename in os.listdir(inputFolder + "/" + test):
                start = time.time()
                Clean_Story(input_name=filename, input_folder=inputFolder + "/" + test, \
                             output_name="data/clean/clean_" + filename)
                print "Story cleaning time:"
                print time.time() - start


        # start = time.time()
        # Clean_Story(input_name = "2016-01-storydata.csv", input_folder="~/PycharmProjects/rvpk", \
        #             output_name = "2016-01-storydata_clean.csv")
        # print "story cleaning time:"
        # print time.time() - start
