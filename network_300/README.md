# Network Security 300

![alt text](../images/net300wc.jpg "Aggregated From Lesson Files")


### Topics
------

* Browser Breakdown
* Interception Proxies
* Web App Basics
    * HTML, CSS, Javascript
* The Stack
* Web Servers
    * Apache, Nginx, IIS
* Server-Side Code
    * PHP, ASP, JSP
    * Python, Ruby, Bash, Perl, etc.
* LAMP Stack
* Session Management
    * Cookies
* Web Server Security and Hardening
* Javascript
    * Why it Matters
    * Background
    * Building Blocks
    * Events
    * Behavior
* Same Origin Policy
    * Defeating SOP
* CORS
* MySQL
    * Planning
    * Security
* Authentication
* Processing Input
* Password Storage
* Authorization
    * Principal of Least Privilege
* APIs
* SOAP
* REST


### Website Created
-----
* [webapp (LAMP Stack)] - Web App with Login System

[webapp (LAMP Stack)]: ./webapp

### Assignments
------
**The goal of NET300 was to build a basic LAMP stack web app for simple signup/login/logout functionality to be exploited in NET400**

* HTTP proxy exploration with both Burp and ZAP.
* Write 3 pages of HTML and link them together and then incorporate javascript and behavioral elements. 
* Install required software to get a LAMP stack up and running and then enable SSL.
* Create the basic framework for the web app using HTML, CSS and PHP.
* Incorporate a password strength meter/checker into the web application. 
* Modify Apache configurations to remediate default headers, directory browsing and default error pages.
* Incorporate javascript into the web app to provide functionality to the user.
* Utilize javascript in the web app to perform client-side checks. 
* Create, setup and configure database to the web application.
* Modify PHP to sanitize user inputs.
* Create administrative account authorization on the web app.


### Tools
------

* Firefox
* Burp
* OWASP's ZAP
* HTML
* CSS
* Javascript
* LAMP Stack
    * Linux
    * Apache
    * MySQL
    * PHP


### Command Line Things
------

* netstat -natlp
* service httpd start
* /etc/init.d/mysqld start
* /var/log/httpd/access.log
* /var/log/httpd/error.log
* /var/log/mysqld.log
* mod_ssl
* mod_security