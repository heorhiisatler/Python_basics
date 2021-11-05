def benchmark(func):
    import time
    
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')

fetch_webpage()
print(fetch_webpage)

db.createUser({
   user : "heorhii",
   pwd : "12345",
   roles : ["readWrite", "dbAdmin"]
});