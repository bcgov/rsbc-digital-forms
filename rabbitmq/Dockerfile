FROM rabbitmq:3.8

# TODO - modify this container to run as non-root

RUN rabbitmq-plugins enable --offline rabbitmq_management

# extract "rabbitmqadmin" from inside the "rabbitmq_management-X.Y.Z.ez" plugin zipfile
# see https://github.com/docker-library/rabbitmq/issues/207
RUN set -eux; \
	erl -noinput -eval ' \
		{ ok, AdminBin } = zip:foldl(fun(FileInArchive, GetInfo, GetBin, Acc) -> \
			case Acc of \
				"" -> \
					case lists:suffix("/rabbitmqadmin", FileInArchive) of \
						true -> GetBin(); \
						false -> Acc \
					end; \
				_ -> Acc \
			end \
		end, "", init:get_plain_arguments()), \
		io:format("~s", [ AdminBin ]), \
		init:stop(). \
	' -- /plugins/rabbitmq_management-*.ez > /usr/local/bin/rabbitmqadmin; \
	[ -s /usr/local/bin/rabbitmqadmin ]; \
	chmod +x /usr/local/bin/rabbitmqadmin; \
	apt-get update; apt-get install -y --no-install-recommends python3; rm -rf /var/lib/apt/lists/*; \
	rabbitmqadmin --version

RUN rabbitmq-plugins enable rabbitmq_shovel rabbitmq_shovel_management

# Copy the create_queue.sh script to the image
# COPY init.sh /usr/local/bin/init.sh
# RUN chmod +x /usr/local/bin/init.sh

COPY definitions.json /etc/rabbitmq/definitions.json
COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

EXPOSE 15671 15672

# CMD ["/usr/local/bin/init.sh"]
