import json
import requests
from plotly.graph_objs import Bar,Layout
from plotly import offline

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
header={'Accept': 'application/vnd.github.v3+json'}
r=requests.get(url,headers=header)
print(f'status code: {r.status_code}')

response_dict=r.json()
filename='response_ditionary.json'
with open(filename,'w') as f:
    json.dump(response_dict,f,indent=4)

repo_dicts=response_dict['items']
repo_names, repo_stars=[],[]

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    repo_stars.append(repo_dict['stargazers_count'])

data=[
    {
        'type': 'bar',
        'x':repo_names,
        'y':repo_stars,
        'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}},
        'opacity': 0.6
    }
]

my_layout={
        'title': 'Most-Starred Python Projects on GitHub',
        'xaxis': {'title': 'Repository'},
        'yaxis': {'title': 'Stars'},
        }

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')