"# webCrawler" 

Put ==webCrawler.pyc== in the same path as your python file. Meanwhile, it is necessary to install ==retry== module in your system.

Sample usage：

1. normal usage
```
import webCrawler as wc

url=r'https://xxxxxxxxxxxxxx'
html=wc.HTML(url)

print html
```

2. get html by using ==proxies==

```
import webCrawler as wc

proxy={'xxx.xxx.xxx.xxx','1234'}
url=r'https://xxxxxxxxxxxxxx'
html=wc.use_requests_proxy(url,proxy)

print html
```
