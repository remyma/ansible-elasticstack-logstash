# Ansible Elasticstack Logstash

Install and configure logstash.

## Requirements

* *java* : logstash needs java to run. This role can handle java install for you. But you can also install it on your own. 

## Role Variables

| Variable     | Default       | Description    |
| ------------ | ------------- | -------------- |
| logstash_java_install | true | true to install java / false if java is already installed on you own |
| logstash_update_java | false | if true, will update java |
| logstash_major_version | 5.x | Major version of logstash to install |
| logstash_pipelines | [] | List of logstash pipelines to deploy |


## Example Playbook


### Basic install

    - hosts: logstash-servers
      roles:
        - { role: ansible-elasticstack-logstash }

### Deploy pipelines

If you want to deploy pipelines on your logstash server, you can override ***logstash_pipelines*** variable.
Place you pipelines .conf files under your ansible project in files/logstash/pipelines/ directory.

    - hosts: 
      roles:
        - { role: ansible-elasticstack-logstash }
      vars:
        logstash_pipelines:
            - my-pipeline.conf
            - second-pipeline.conf
    

## License

BSD


