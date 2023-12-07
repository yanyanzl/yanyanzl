# Web Basics



### Synchoronous Web
- Legacy web applications are synchronous in nature. The user interacts with the web interface presented in the browser, the browser makes requests back to the server based on that user interaction, and the server responds to those requests with new presentation for the user - fundamentally a synchronous process.


### Asynchronous Web
- In the Asynchronous Web it is possible to deliver spontaneous presentation changes to the user as the state of a dynamic system changes, without the need for the user to interact with the interface.

- ways:
    - option 1: HTTP streaming, where multiple responses can be sent to a single request, as illustrated below. This is an efficient mechanism, but unfortunately is not ubiquitously acceptable across all proxy/firewall configurations, making it unsuitable for general purpose deployments.
    - option 2: HTTP long polling, where the request is made in anticipation of a future response, but that response is blocked until some event occurs that triggers its fulfillment. This mechanism, which is illustrated below, is nearly as efficient as streaming and is completely compatible with proxy/firewall configurations as it is indistinguishable from a slow responding server.
    
    
    