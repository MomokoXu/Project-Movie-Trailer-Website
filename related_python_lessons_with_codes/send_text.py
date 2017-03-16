from twilio.rest import TwilioRestClient
# equavlent to from twilio import rest, then client = rest.TwilioRestClient(..., ...)

account_sid = "AC13a66020fba9943b41f63906d2b78d37"
auth_token = "8e999f0e5716a42fbd34615a3aab7a80"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body = "Lalalala!Fighting!", to = "+19295227155", from_ = "+14156500808")
print message.sid