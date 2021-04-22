# %%
from urllib.parse import urlencode, unquote
import requests
import json

url = 'https://tour.chungbuk.go.kr/openapi/tourInfo/stay.do'


queryString = "?" + urlencode(
    {
        "key" : "result",
        "type" : "json",
        #"sdate" : "20210422", 
        #"stdHour" : "06" 
    }
)
print(queryString)
response = requests.get(url + queryString)
print("===== response json data start =====")
print(response)
print("===== response json data end =====")
print()
r_dict = json.loads(response.text)
r_list = r_dict.get("result")

#print(r_list) # None으로 출력된다 왜...?

#r_dict = json.loads(response.text)
#r_list = r_dict.get("list")
#r_unitNames = r_list.get("unitName")


result = {}
for item in r_list: 
    print(item.get("tourSe") + item.get("tourNm") +item.get("adres")) # key value로 쌍으로 가져온다. 
    
        
#print("===== response dictionary(python object) data start =====")
#print(result)
#print("===== response dictionary(python object) end =====")
#print()
# %%
