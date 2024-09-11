import json
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

filename='data/earthquakes1970-2014.json'

with open(filename) as f:
    read_eq_data=json.load(f)

eq_dicts=read_eq_data['features']
mags,lons,lats,hover_texts=[],[],[],[]

for eq_dict in eq_dicts:
    mag=eq_dict['properties']['Magnitude']
    lon=eq_dict['properties']['Longitude']
    lat = eq_dict['properties']['Latitude']
    title=eq_dict['properties']['Depth']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[2*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }

}]
my_layout=Layout(title="Global Earthquakes")

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='globalearthquakes1974-24.html')

