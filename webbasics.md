# Web Basics



### Synchoronous Web
- Legacy web applications are synchronous in nature. The user interacts with the web interface presented in the browser, the browser makes requests back to the server based on that user interaction, and the server responds to those requests with new presentation for the user - fundamentally a synchronous process.


### Asynchronous Web
- In the Asynchronous Web it is possible to deliver spontaneous presentation changes to the user as the state of a dynamic system changes, without the need for the user to interact with the interface.

- ways:
    - option 1: HTTP streaming, where multiple responses can be sent to a single request, as illustrated below. This is an efficient mechanism, but unfortunately is not ubiquitously acceptable across all proxy/firewall configurations, making it unsuitable for general purpose deployments.
    - option 2: HTTP long polling, where the request is made in anticipation of a future response, but that response is blocked until some event occurs that triggers its fulfillment. This mechanism, which is illustrated below, is nearly as efficient as streaming and is completely compatible with proxy/firewall configurations as it is indistinguishable from a slow responding server.
    
    

### Bringing Matplotlib to the Browser
- The mpld3 package is extremely easy to use: you can simply take any script generating a matplotlib plot, run it through one of mpld3’s convenience routines, and embed the result in a web page.
    - pip install mpld3
    
### Jinja : A very fast and expressive HTML template engine
- Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.
- pip install -U Jinja2
```sh
😀🍏🍎
{% extends "base.html" %}
{% block title %}Members{% endblock %}
{% block content %}
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>
{% endblock %}
🍌🍉🍇

```

### Chart for Website
1. D3.js (also known as D3, short for Data-Driven Documents) is a JavaScript library for producing dynamic, interactive data visualizations in web browsers. It makes use of Scalable Vector Graphics (SVG), HTML5, and Cascading Style Sheets (CSS) standards. It is the successor to the earlier Protovis framework.[2] Its development was noted in 2011,[3] as version 2.0.0 was released in August 2011.[4] With the release of version 4.0.0 in June 2016, D3 was changed from a single library into a collection of smaller, modular libraries that can be used independently.[5]
    - install Django packages: Django REST Pandas by command: pip install rest-pandas
        - Django REST Pandas (DRP) provides a simple way to generate and serve pandas DataFrames via the Django REST Framework. The resulting API can serve up CSV (and a number of other formats for consumption by a client-side visualization tool like @wq/analyst.

        - The design philosophy of DRP enforces a strict separation between data and presentation. This keeps the implementation simple, but also has the nice side effect of making it trivial to provide the source data for your visualizations. This capability can often be leveraged by sending users to the same URL that your visualization code uses internally to load the data.

        - While DRP is primarily a data API, it also provides a default collection of interactive visualizations through the @wq/chart library, and a @wq/pandas loader to facilitate custom JavaScript charts that work well with CSV output served by DRP. These can be used to create interactive time series, scatter, and box plot charts - as well as any of the other charting possibilities Plotly provides.

2. Chart.js is a free, open-source JavaScript library for data visualization, which supports eight chart types: bar, line, area, pie (doughnut), bubble, radar, polar, and scatter. Created by London-based web developer Nick Downie in 2013, now it is maintained by the community and is the second most popular JavaScript charting library on GitHub by the number of stars after D3.js, considered significantly easier to use though less customizable than the latter. Chart.js renders in HTML5 canvas and is widely covered as one of the best data visualization libraries. It is available under the MIT license


3. four most popular Python plotting libraries—Matplotlib, Seaborn, Plotly, and Bokeh—plus a couple of great up-and-comers to consider: Altair, with its expressive API, and Pygal, with its beautiful SVG output. I'll also look at the very convenient plotting API provided by pandas.
    - Matplotlib is the oldest Python plotting library, and it's still the most popular. It was created in 2003 as part of the SciPy Stack, an open source scientific computing library similar to Matlab.
        - Matplotlib gives you precise control over your plots—for example, you can define the individual x-position of each bar in your barplot. Here is the code to graph this
    
    - Seaborn is an abstraction layer on top of Matplotlib; it gives you a really neat interface to make a wide range of useful plot types very easily.
        - It doesn't compromise on power, though! Seaborn gives escape hatches to access the underlying Matplotlib objects, so you still have complete control.
        - Seaborn's code is simpler than the raw Matplotlib
        
    - Plotly is a plotting ecosystem that includes a Python plotting library. It has three different interfaces:

        - An object-oriented interface
        - An imperative interface that allows you to specify your plot using JSON-like data structures
        - A high-level interface similar to Seaborn called Plotly Express
        - Plotly plots are designed to be embedded in web apps. At its core, Plotly is actually a JavaScript library! It uses D3 and stack.gl to draw the plots.
        - You can build Plotly libraries in other languages by passing JSON to the JavaScript library. The official Python and R libraries do just that.
        
    - Bokeh (pronounced "BOE-kay") specializes in building interactive plots, so this standard example doesn't show it off to its best. Like Plotly, Bokeh's plots are designed to be embedded in web apps; it outputs its plots as HTML files.
    
    - Altair is based on a declarative plotting language (or "visualization grammar") called Vega. This means it's a well-thought-through API that scales well for complex plots, saving you from getting lost in nested-for-loop hell.
        - As with Bokeh, Altair outputs its plots as HTML files. 
        
    - Pygal focuses on visual appearance. It produces SVG plots by default, so you can zoom them forever or print them out without them getting pixellated. Pygal plots also come with some good interactivity features built-in, making Pygal another underrated candidate if you're looking to embed plots in a web app.
    
    -Pandas is an extremely popular data science library for Python. It allows you to do all sorts of data manipulation scalably, but it also has a convenient plotting API. Because it operates directly on data frames, the pandas example is the most concise code snippet in this article—even shorter than the Seaborn code!
        - The pandas API is a wrapper around Matplotlib, so you can also use the underlying Matplotlib API to get fine-grained control of your plots.