import scrapy


class LinkedInSpider(scrapy.Spider):
    name = "linkedin"

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        urls = [
            'https://stackoverflow.com/jobs',
            'https://stackoverflow.com/jobs?pg=2',
            'https://stackoverflow.com/jobs?pg=3',
            'https://stackoverflow.com/jobs?pg=4',
            'https://stackoverflow.com/jobs?pg=5',
            'https://stackoverflow.com/jobs?pg=6',
            'https://stackoverflow.com/jobs?pg=7',
            'https://stackoverflow.com/jobs?pg=8',
            'https://stackoverflow.com/jobs?pg=9',
            'https://stackoverflow.com/jobs?pg=10'
        ]

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        for title in response.css('h2.g-col10'):
            yield {'title': title.css('a ::text').extract_first()}
        page = response.url.split("/")[-2]
        filename = 'linked_in_pages-%s.csv' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
