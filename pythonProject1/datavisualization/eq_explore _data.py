import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename='data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)

readable_file='data/readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dict=all_eq_data['features']
print(len(all_eq_dict))

mags,lons,lats=[],[],[]
for eq_dict in all_eq_dict:
    mag=eq_dict['properties']['mag']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)

# Map the earthquakes.
data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }

}]
my_layout=Layout(title="Global Earthquakes")

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='globalearthquakes.html')

