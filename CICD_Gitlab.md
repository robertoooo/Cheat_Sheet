# Basic formatting of the .gitlab-ci.yml
```yml
stages:
  - build
  - test

build the car:
  image: node
  stage: build
  script:
    - mkdir build
    - cd build
  artifacts:
    paths:
      - build/
```


## Installing GitLab Runner & Configure own runners
https://docs.gitlab.com/runner/install/windows.html#installation
https://docs.gitlab.com/runner/register/index.html




















# Gatsby CLI
Host a very easy unsecure website on the Internet
```cli
npm install -g gatsby-cli 
gastby new gastby-site    #Create a new site


gatsby develop            #Start development server.


```
