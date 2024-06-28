'''
HTTP method requests
get -> to fetch the data
post -> sending the data
delete -> deleting the data
put -> modifying the data

http://www.boredapi.com/api/activity
https://api.chucknorris.io/jokes/random
'''
import json
import requests

url = 'https://randomuser.me/api/'

def call_api(url):
    try:

        res = requests.get(url)
        # print(res)
        # print("status code: ", res.status_code)
        # print("data: ", res.text)
        # print(type(res))
        data= res.text
        # print(type(data))

        # TODO: convert str data into dictionary
        data = json.loads(data)
        # print(type(data))
        return data
    except BaseException as e:
        print("ERROR: ",e)

def main():
    res = call_api(url)
    # print(res)
    fname = res["results"][0]["name"]["first"]
    lname = res["results"][0]["name"]["last"]
    print(fname , lname)

if __name__ == '__main__':
    main()
