# CI/CD basics

### what is CI/CD

1. CI/CD bridges the gaps between development and operation activities
- teams by enforcing automation in building, testing and deployment of applications. 
- CI/CD services compile the incremental code changes made by developers, 
- then link and package them into software deliverables. 
- Automated tests verify the software functionality, 
- and automated deployment services deliver them to end users. 
- The aim is to increase early defect discovery, increase productivity, 
- and provide faster release cycles. 
- The process contrasts with traditional methods where a collection of software updates
- were integrated into one large batch before deploying the newer version. 
- Modern-day DevOps practices involve:

- continuous development,
- continuous testing,
- continuous integration,
- continuous deployment, and
- continuous monitoring
- of software applications throughout its development life cycle. 
- The CI/CD practice, or CI/CD pipeline, forms the backbone of modern day DevOps operations.

## CI/CD platform Jenkins

### jenkins LTS long-term-support version
### jenkins weekly: weekly released version

- Jenkins is an extensible automation server with more than 1800 plugins 
- providing integrations for hundreds of tools and services. 
- Jenkins is a self-contained, open source automation server 
- which can be used to automate all sorts of tasks related to building, 
- testing, and delivering or deploying software.

- Jenkins can be installed through native system packages, Docker, 
- or even run standalone by any machine with a Java Runtime Environment (JRE) installed.

### 1. installation :
```sh
Install the latest LTS version: brew install jenkins-lts
Start the Jenkins service: brew services start jenkins-lts
Restart the Jenkins service: brew services restart jenkins-lts
Update the Jenkins version: brew upgrade jenkins-lts

```

