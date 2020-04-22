COMMON_OVERLAYS = tkl-webcp apache
COMMON_CONF = apache-vhost apache-credit tkl-webcp

CREDIT_ANCHORTEXT = OTRS Appliance
NONFREE = y

include $(FAB_PATH)/common/mk/turnkey/mysql.mk
include $(FAB_PATH)/common/mk/turnkey.mk
