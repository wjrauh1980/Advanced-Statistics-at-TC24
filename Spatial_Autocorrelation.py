import pandas as pd
import geopandas as gpd
from pysal.lib import weights
from pysal.explore import esda

def calculate_morans_i(_arg1):
    print('were printing arg1')
    print(_arg1)
    df = pd.DataFrame(_arg1)
    print(df)
    df_housing = df[['longitude', 'latitude', 'product_rating']]
    # Convert the DataFrame to a GeoDataFrame
    gdf = gpd.GeoDataFrame(df_housing, geometry=gpd.points_from_xy(df_housing['longitude'], df_housing['latitude']))

    # Create a spatial weights matrix. Adjust `k` as necessary for your data.
    w = weights.KNN.from_dataframe(gdf, k=2)  # k-nearest neighbors

    # Row-standardize the weights
    w.transform = 'R'

    # Calculate Moran's I
    mi = esda.moran.Moran(gdf['product_rating'], w)
    stat_df = pd.DataFrame([mi.I], columns=['I'])
    stat_df['p'] = mi.p_sim
    return stat_df


return calculate_morans_i(_arg1).to_dict(orient='list')