""" Copyright start
  Copyright (C) 2008 - 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """


from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from .operations import operations, check_health


logger = get_logger('fortinet-forticnapp')


class Lacework(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            config['connector_info'] = {"connector_name": self._info_json.get('name'),
                                        "connector_version": self._info_json.get('version')}
            operation = operations.get(operation)
            return operation(config, params)
        except Exception as Err:
            logger.error('Exception occurred: {}'.format(Err))
            raise ConnectorError(Err)

    def check_health(self, config):
        config['connector_info'] = {"connector_name": self._info_json.get('name'),
                          "connector_version": self._info_json.get('version')}
        return check_health(config)
