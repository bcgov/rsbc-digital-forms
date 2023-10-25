#!/bin/bash

rabbitmq-server -detached
# Wait for RabbitMQ to start
sleep 10

# Declare a queue using the RabbitMQ CLI tool
rabbitmqadmin declare queue name=df-storage-events durable=true auto_delete=false --vhost=/

# Bind the queue to the AMQ.direct exchange
# rabbitmqadmin declare binding source=AMQ.direct destination_type=queue destination=df-storage-events routing_key=dfevents