# Test Basics


### automated test

- Selenium : website test automation
- Selenium allows users to simulate common activities performed by end-users; entering text into fields, selecting drop-down values and checking boxes, and clicking links in documents. It also provides many other controls such as mouse movement, arbitrary JavaScript execution, and much more.
    1. If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs. WebDriver uses browser automation APIs provided by browser vendors to control the browser and run tests. This is as if a real user is operating the browser. Since WebDriver does not require its API to be compiled with application code, it is not intrusive. Hence, you are testing the same application which you push live.
    
    2. IDE (Integrated Development Environment) is the tool you use to develop your Selenium test cases. It’s an easy-to-use Chrome and Firefox extension and is generally the most efficient way to develop test cases. It records the users’ actions in the browser for you, using existing Selenium commands, with parameters defined by the context of that element. This is not only a time-saver but also an excellent way of learning Selenium script syntax.

    3. Selenium Grid allows you to run test cases in different machines across different platforms. The control of triggering the test cases is on the local end, and when the test cases are triggered, they are automatically executed by the remote end.



### When testing, more is better
    - It doesn’t matter. Let them grow. For the most part, you can write a test once and then forget about it. It will continue performing its useful function as you continue to develop your program.
    - Sometimes tests will need to be updated., so to that extent tests help look after themselves.
    - a separate TestClass for each model or view
    - a separate test method for each set of conditions you want to test
    - test method names that describe their function