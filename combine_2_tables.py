import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """Uses merge function.2 personIds specified using r and left. How left means only matching rows from the address df will be included, resulting in the 4 rows  """
    df = pd.merge(left=person, right=address, how='left',on='personId')[['firstName','lastName','city','state']]
    return df