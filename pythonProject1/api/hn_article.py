import json
from operator import itemgetter

import requests

filename='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(filename)

submission_ids=r.json()
submission_dicts=[]

for submission_id in submission_ids[:10]:
    url=f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r=requests.get(url)
    response_dict=r.json()

    submission_dict={
        'title':response_dict['title'],
        'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
        'comments':response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts=sorted(submission_dicts,key=itemgetter('comments'),reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
