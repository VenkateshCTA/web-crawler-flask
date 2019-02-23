from flask import Flask, redirect, url_for, request, render_template
import requests
from parsel import Selector

# Flask App
app = Flask(__name__)

# Home page route
@app.route('/')
def home_page():
    """
    Home Page API
    :return: Contents of the index.html page
    """
    return render_template('index.html')

# Results page API
@app.route('/results', methods=['POST'])
def links():
    """
    Results Page API
    :return: Content requested from the user
    """
    url = str(request.form['url'])
    depth = int(request.form['depth'])
    response = requests.get(url)
    selector = Selector(response.text)
    href_links = selector.xpath('//a/@href').getall()
    links = []
    all_images = {}
    imgs = []
    if depth == 1:
        res = [k for k in href_links if url in k]
        links = set(res)

    elif depth == 2:
        image_links = selector.xpath('//img/@src').getall()
        links = url.split()
        imgs = set(image_links)

    elif depth == 3:
        res = [k for k in href_links if url in k]
        links = set(res)
        for link in links:
            try:
                response = requests.get(link)
                if response.status_code == 200:
                    image_links = selector.xpath('//img/@src').getall()
                    all_images[link] = image_links
                    imgs = set(all_images[link])
            except Exception as exp:
                print('Error navigating to link : ', link)

    return render_template('show_links_images.html', items=links, imgs=imgs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
