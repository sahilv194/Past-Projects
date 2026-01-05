import pandas as pd

def convert_to_time(time_value):
    if isinstance(time_value, str):
        return pd.to_datetime(time_value).time()
    elif hasattr(time_value, 'time'):
        return time_value.time()
    elif pd.isna(time_value):
        raise ValueError("Time value cannot be empty")
    return time_value

def convert_to_date(date_value):
    if isinstance(date_value, str):
        return pd.to_datetime(date_value).date()
    elif hasattr(date_value, 'date'):
        return date_value.date()
    elif pd.isna(date_value):
        raise ValueError("Date value cannot be empty")
    return date_value

def parse_excel_to_dict(source):
    df = pd.read_excel(source)

    df['date'] = df['date'].apply(convert_to_date)
    df['start_time'] = df['start_time'].apply(convert_to_time)
    df['end_time'] = df['end_time'].apply(convert_to_time)

    data_dict = df.to_dict(orient='records')
    return data_dict
