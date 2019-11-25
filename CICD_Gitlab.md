# Basic formatting of the .gitlab-ci.yml
```yml
stages:
  - build
  - test

build the car:
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
