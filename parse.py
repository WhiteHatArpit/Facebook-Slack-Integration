import json

# parse fetched message data
def parse(data):
    
    total_unread = data['inbox']['summary']['unread_count']
    
    packet = "\n###############################################\n\n"
    packet += "no. of People who messaged me: " + str(total_unread)

    user = 0
    while total_unread > 0:
        
        unread = data['inbox']['data'][user]['unread']
        if unread:
            packet += "\n\n-------------------------------------------------------------------------------\n\n"
            packet += "From: " + str( data['inbox']['data'][user]['comments']['data'][-1]['from']['name'] )
            for i in range(-unread,0):
                packet += "\n"+str( data['inbox']['data'][user]['comments']['data'][i]['message'] )
            total_unread -= 1
        user += 1
        
    packet += "\n\n###############################################\n"
    return packet

# parse fetched notifications data
def parsenotif(data):
    
    packet = "\n###############################################\n\n"

    total_unseen = data['notifications']['summary']['unseen_count']
    packet += "no. of new Notifications for me: " + str(total_unseen)

    unseen = len(data['notifications']['data'])
    for i in range(unseen):
        packet += "\n\n-------------------------------------------------------------------------------\n\n"
        packet += "From: " + str( data['notifications']['data'][i]['from']['name'] )
        packet += "\n" + str( data['notifications']['data'][i]['title'] )

    packet += "\n\n###############################################\n"
    return packet