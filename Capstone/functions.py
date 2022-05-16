
import pandas as pd
import os
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import time
import joblib

def log(text):
    file_name = time.strftime("%Y%m%d-%H%M%S")
    f = open("./logs/" + file_name + ".txt", "w")
    f.write(str(text))
    f.close()

def get_data(folder_name):
    df = pd.DataFrame()

    data_files = [f for f in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, f))]
    data_files = sorted(data_files)

    for f in data_files:
        invoice_df = pd.read_json(os.path.join(folder_name, f))
        
        # Rename column names
        invoice_df = invoice_df.rename(columns={
            'total_price': 'price',
            'StreamID': 'stream_id',
            'TimesViewed': 'times_viewed',
            'invoice': 'invoice_id'
        })
        
        df = df.append(invoice_df)

    return df

def clean_data(df):
    df['invoice_id'] = df['invoice_id'].str.replace(r'\D', '')
    df = df[df['price'].between(df['price'].quantile(0.01), df['price'].quantile(0.99))]

    df_clean = df[['year', 'month', 'day', 'times_viewed', 'price', 'country']]

    return df_clean

def get_ts(df):
    df_daily = df.groupby(['year', 'month', 'day']).agg({'times_viewed':'sum', 'price':'sum','country':'first'}).reset_index()
    df_daily['date'] = pd.to_datetime(df_daily[['year', 'month', 'day']])
    ts_daily = df_daily[['date','times_viewed']]
    ts_daily.set_index('date', inplace=True)
    ts_daily = ts_daily.asfreq(freq='1D')
    ts_daily['times_viewed'].interpolate(inplace = True)

    return ts_daily

def train_model(folder_name='./ai-workflow-capstone-master/cs-train'):
    df = get_data(folder_name)
    df_clean = clean_data(df)
    ts_daily = get_ts(df_clean)

    model = ExponentialSmoothing(ts_daily)
    model = model.fit()

    log(model.summary())

    joblib.dump(model, './models/model.joblib')

def get_model():
    return joblib.load('./models/model.joblib')

def model_predict(start_date, end_date):
    model = get_model()
    print(start_date, end_date)
    predictions = model.predict(start=start_date, end=end_date)

    return predictions