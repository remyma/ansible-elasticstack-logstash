# Ansible Elasticstack Logstash

Install and configure logstash.

## Requirements

* *java* : logstash needs java to run. This role can handle java install for you. But you can also install it on your own. 

## Role Variables

| Variable     | Default       | Description    |
| ------------ | ------------- | -------------- |
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


