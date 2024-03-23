import requests

f = open('test.log', 'w+')
def saveResult(name, url, result):
 f.write('Test name:' + str(name) + '\n')
 f.write('Test URL:' + str(url) + '\n')
 f.write('Test result:' + str(result) + '\n')
 f.write('---------------------------------------------\n ')
 def checkServiceForWord(url, keyword):
        result = False
        try:
                x = requests.get(url)
                print(x.text)
                if keyword in x.text:
                        print("found keyword")
                        result=True
        except:
                print("error")
                result= False
 return result

# Test 1
name = 'Test 1'
url = 'http://localhost:5000/’'
result = checkServiceForWord(url, 'URl')
saveResult(name, url, result)
print(result)

# Test 2
name = 'Test 2'
url = 'http://localhost:5000/getProducts’'
result = checkServiceForWord(url, 'banana')
saveResult(name, url, result)
print(result)

# Test 3
name = 'Test 3'
url = 'http://127.0.0.1:5000/insertProducts?api_key=login’'
result = checkServiceForWord(url, 'inserted')
saveResult(name, url, result)
print(result)

# Test 4
name = 'Test 4'
url = 'http://127.0.0.1:5000/insertProducts’'
result = checkServiceForWord(url, 'Invalid')
saveResult(name, url, result)
print(result)

# Test 5
name = 'Test 5'
url = 'http://127.0.0.1:5000/getTitles’'
result = checkServiceForWord(url, 'banana')
saveResult(name, url, result)
print(result)
# finish up
f.close()