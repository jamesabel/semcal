#!/usr/bin/env bash
#
# 1) do a "$source activate.sh" to activate this project's Python virtual environment
# 2) do a "$zappa init" before executing these steps.  That will create a zappa_settings.json.
# 3) edit the zappa_settings.json to add the "domain" and "certificate_arn" items.
#    The certificate ARN can be found at https://console.aws.amazon.com/acm (navigate to the certificate for this
#    app's domain).
#
zappa deploy dev
zappa certify --yes
zappa update dev
