import parsel


bar=parsel.Selector(html)

a1 = bar.css('a').getall()

a2 = bar.css('a.test').get()#class

a3 = bar.css('a#test').get()#id

a4 = bar.css('a>b').getall()

a5 = bar.css('a::text').get()

a6 = bar.css('a.b.c').getall()

a7 = bar.css('a::attr(href)').get()














