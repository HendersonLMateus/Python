from twilio.rest import Client


account_sid = "AC74a64e6691e7534b439dad76ae5d74b9"
auth_token  = "b16b0e6cc912163c91cdb0a8534f9004"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5585981222155", 
    from_="+12028165995",
    body="Negro")

print(message.sid)
