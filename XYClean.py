import pandas as pd
import datetime as dt

## Create a the y columns
def create_column(df, new_column = 'CSS_score', compare_column = 'CSS'):
    df.ix[df[compare_column] == 50, new_column] = 0
    df.ix[df[compare_column] > 50, new_column] = 1
    df.ix[df[compare_column] < 50, new_column] = -1
    return df

## Split data into training and test based on a date
def split(df, test_start_string = '2016-12-01', date_fmt = '%Y-%m-%d'):
    '''
    test_start_string: string: 'yyyy-mm-dd'
        date entered is starting date for testing set
    return: train, test
    '''
    test_start = dt.datetime.strptime(test_start_string,date_fmt).date()
    train_end = test_start - dt.timedelta(days = 1)
    train_end_string = train_end.strftime(date_fmt)
    train = df.ix[:train_end_string]
    test = df.ix[test_start_string:]
    
    return train, test
    
## Load data from csv file    
def load(filename, parse_dates = ['TIMESTAMP_UTC'], index_col = 'TIMESTAMP_UTC'):
    return pd.read_csv(filename, parse_dates = parse_dates, index_col = index_col)

## split into XY lists
def XYsplit(df, X_column = 'HEADLINE', Y_column = 'CSS_score'):
    X = df[X_column]
    Y = df[Y_column]
    return X.tolist(), Y.tolist()

if __name__ == "__main__":
    filename = "2016_clean.csv"
    filepath = "./appended/"
    df = load(filepath+filename)
    df = create_column(df)
    train, test = split(df)
    X_train, Y_train = XYsplit(train)
    X_test, Y_test = XYsplit(test)
