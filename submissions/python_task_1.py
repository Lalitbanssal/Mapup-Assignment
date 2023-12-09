import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values,
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    df=pd.read_csv('dataset-1.csv')
    df= df.pivot(index='id_1', columns='id_2', values='car')
    df.fillna(0, inplace=True)

    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    def label(car):
      if car<=15:
        return "low"
      elif car>15 and car<=25:
        return "medium"
      else:
        return "high"

    df['car_type']=df['car'].apply(label)
    car_type_count=df['car_type'].value_counts()
    car_type_count=sorted(dict(car_type_count).items())

    return dict(car_type_count)


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    bus_mean_value=df['bus'].mean()
    index_value=df[df['bus']>2*bus_mean_value].index

    return list(index_value.sort_values())


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    filtered_route=df.groupby('route')['truck'].mean()
    filtered_route=filtered_route[filtered_route>7].index

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    dup_matrix=matrix.copy()
    dup_matrix[matrix>20]*=0.75
    dup_matrix[matrix<=20]*=1.25
    dup_matrix=dup_matrix.round(1)

    return dup_matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()


