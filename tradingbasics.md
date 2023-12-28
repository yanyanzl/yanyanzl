# trading platform basics

## TWS IB

### set up

    1. Download API: 
        - It is important to know that the TWS API is only available through the interactivebrokers.github.io MSI or ZIP file
    
    2. Config on TWS: API configuration
    
    3. change python enviorenment:
        - firtsly, you should then change their directory to  {TWS API}\source\pythonclient
        - secondlyl, you need to run the setup.py steps with the installation parameter. This can be done with the command: python setup.py install
        - finnaly, Confirm your installation:
            - show the latest installed version on your system: python -m pip show ibapi
        - Alternatively, take the ibapi folder from within the pythonclient folder and place it in the directory you are creating your scripts to access the API from.    
        
    4. The TWS API is a programming interface to TWS, and as such, for an application to connect to the API there must first be a running instance of TWS or IB Gateway.
    
    5. trouble shooting:
        - Log Files
        - TWS and IB Gateway can be configured to create a separate log file which has a record of just communications with API applications. This log is not enabled by default; but needs to be enabled by the Global Configuration setting “Create API Message Log File”(picture below).
        - Local location of logs: Logs are stored in the TWS settings directory, C:\Jts\ by default on a Windows computer (the default can be configured differently on the login screen).

        - The path to the log file directory can be found from a TWS or IB Gateway session by using the combination Ctrl-Alt-U. This will reveal path such as C:\Jts\detcfsvirl\ (on Windows).
        
        - Due to privacy regulations, logs are encrypted before they are saved to disk. They can be decrypted from the associated TWS or IB Gateway session.
        
        - In TWS: Classic TWS  Help -> Troubleshooting -> Diagnostics -> TWS Logs.
        
    6. Architecture
        - Receiving information: The IBApi.EWrapper interface is the mechanism through which the TWS delivers information to the API client application. By implementing this interface the client application will be able to receive and handle the information coming from the TWS.
            - class TestWrapper(wrapper.EWrapper):

        - Sending information: The class used to send messages to TWS is IBApi.EClientSocket. Unlike EWrapper, this class is not overriden as the provided functions in EClientSocket are invoked to send messages to TWS. To use EClientSocket, first it may be necessary to implement the IBApi.EWrapper interface as part of its constructor parameters so that the application can handle all returned messages. Messages sent from TWS as a response to function calls in IBApi.EClientSocket require an EWrapper implementation so they can be processed to meet the needs of the API client.
            - class TestClient(EClient):
                 def __init__(self, wrapper):
                     EClient.__init__(self, wrapper)
            ...
            - class TestApp(TestWrapper, TestClient):
                  def __init__(self):
                  TestWrapper.__init__(self)
                         TestClient.__init__(self, wrapper=self)
                         
        - For the most part, the EClient handles all outgoing requests while the EWrapper handles incoming messages. True to its name, EWrapper acts like a wrapper for incoming messages and in most cases, a function from it will need to be overwritten in your script to redirect the output to where you want it to go.
                         
    7. Connectivity
        - Once our two main objects have been created, EWrapper and ESocketClient, the client application can connect via the IBApi.EClientSocket object:
            - app.connect("127.0.0.1", args.port, clientId=0)
            - Most commonly error 502 will indicate that TWS is not running with the API enabled, or it is listening for connections on a different socket port.
            
        - After the socket has been opened, there must be an initial handshake in which information is exchanged about the highest version supported by TWS and the API. This is important because API messages can have different lengths and fields in different versions and it is necessary to have a version number to interpret received messages correctly.
        
        - The EReader Thread: API programs always have at least two threads of execution. One thread is used for sending messages to TWS, and another thread is used for reading returned messages. The second thread uses the API EReader class to read from the socket and add messages to a queue. 
        
        - In Python IB API, the code below is included in Client::connect(), so the EReader thread is automatically started upon connection. There is no need for user to start the reader.
        
        - Once the client is connected, a reader thread will be automatically created to handle incoming messages and put the messages into a message queue for further process. User is required to trigger Client::run() below, where the message queue is processed in an infinite loop and the EWrapper call-back functions are automatically triggered.
        
        - Now it is time to revisit the role of IBApi.EReaderSignal initially introduced in The EClientSocket Class. As mentioned in the previous paragraph, after the EReader thread places a message in the queue, a notification is issued to make known that a message is ready for processing. In the (C++, C#/.NET, Java) APIs, this is done via the IBApi.EReaderSignal object we initiated within the IBApi.EWrapper’s implementer. In the Python API, it is handled automatically by the Queue class.
        
        
    8. Reading logs:
        - In our API logs, the direction of the message is indicated by the arrow at the beginning:
    
        ``` plain text
        -> for incoming messages (TWS to client)
        
        <- for outgoing messages (client to TWS)
        
        Thus  <- 3 (outgoing request of type 3) is a placeOrder request, and the subsequent incoming requests are:
        
        -> 5 = openOrder response
        
        -> 11 = executionData response
        
        -> 59 = commissionReport response
        
        Also note that the first openOrder response carries with it an orderStatus response in the same message. If that status were to change later, it would be delivered as a standalone message:
        
        -> 3 = orderStatus response
        ```






        
        