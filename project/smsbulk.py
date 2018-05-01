from twilio.rest import TwilioRestClient
account_sid ="AC17b30a6961c87f182f0f416c0346528c"
auth_token = "ba2c91773816dd6434ba42ba9b88f60b"
clent=TwilioRestClient(account_sid,auth_token)

message=client.sms.messages.create(
    body="My name is Vinay Kumar",
    to ="+919951711931",
    from_="+919985945958"
)
 print(message.sid)