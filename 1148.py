import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views["id"] = np.where(views["author_id"]==views["viewer_id"], 
                           views["author_id"], 
                           np.nan)
    return views[["id"]].dropna().drop_duplicates().sort_values(by="id")