import requests
import json
from googleapiclient.discovery import build
from nse_equity_analysis.database.schema.db_model import AccessTockens
from nse_equity_analysis.database.connection.db_connection import *

api_key=get_session().query(AccessTockens).filter(AccessTockens.provider=='google_search',AccessTockens.tocken_type=='api_key').all()[0].tocken
print(api_key)
moneycontrol_cx =get_session().query(AccessTockens).filter(AccessTockens.provider=='google_search',AccessTockens.tocken_type=='moneycontrol').all()[0].tocken
times_of_india_context =get_session().query(AccessTockens).filter(AccessTockens.provider=='google_search',AccessTockens.tocken_type=='times_of_india').all()[0].tocken


service = build("customsearch", "v1", developerKey=api_key)
def toi_search(query, num_results=20):
    all_results=[]
    for i in range(1, num_results,10):
        res = service.cse().list(q=query, cx=times_of_india_context, num=10, start=i).execute()
        all_results.append(all_results.extend(res['items']))
    for result in all_results:
        if result is None:
            continue
        pagemaps = result['pagemap']
        if 'newsarticle' in pagemaps:
            for newsarticle in pagemaps['newsarticle']:
                published_date = newsarticle['datepublished']
                headline = newsarticle['headline']
                print('{},{}'.format(published_date, headline))


def moneycontrol_search(query, num_result):
    all_results=[]
    for i in range(1,num_result,10):
        res = service.cse().list(q=query, cx=moneycontrol_cx, num=10, start=i).execute()
        all_results.append(all_results.extend(res['items']))

    for item in all_results:
        if item is None:
            continue
        title=item['title']
        if 'pagemap' in item :
            pagemaps = item['pagemap']
            if 'metatags' in pagemaps:
                metatags=pagemaps['metatags']
                for metatag in metatags:
                    if 'last-modified' in metatag:
                        last_modified=metatag['last-modified']
                        print('{}, {}'.format(last_modified, title))

def api_search():
    search_url = 'https://www.googleapis.com/customsearch/v1?key={}&cx={}&q=yes bank,start=0'.format(api_key,
                                                                                                     times_of_india_context)
    result = requests.get(search_url)
    json_result = json.loads(result.text)
    print(json_result)

query='Yes Bank'
num_results=10
moneycontrol_search(query, num_results )





