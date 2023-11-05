 from urllib.request import urlopen

url = "https://www.amazon.in/Lenovo-Display-Speakers-Octa-Core-Processor/dp/B0B8DKL2SD/ref=lp_4363894031_1_1?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&th=1"

page = urlopen(url)

page

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(html)

title_index = html.find("<title>")
title_index

start_index = title_index + len("<title>")

print("Start index is->" ,end_index)

title = html[start_index:end_index]
title

