root.build/ignore-errors = otrs2

COMMON_OVERLAYS = tkl-webcp apache
COMMON_CONF = postfix-local apache-vhost apache-credit tkl-webcp

CREDIT_ANCHORTEXT = OTRS Appliance

include $(FAB_PATH)/common/mk/turnkey/mysql.mk
include $(FAB_PATH)/common/mk/turnkey.mk
