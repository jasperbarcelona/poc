Clone the repository and start it

$ git clone git@git.cocoonlabs.tech:mantis/pldt_mockup
$ cd pldt_mockup
$ docker-compose up -d
```

Dependencies
---

You need to have the following applications installed in your system:

1. docker>=1.13

Known Issues
---

### elasticsearch:5.0.0 max virtual memory areas vm.max_map_count [65530] likely too low, increase to at least [262144]

$ sudo sysctl -w vm.max_map_count=262144