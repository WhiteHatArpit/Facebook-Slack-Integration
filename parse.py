import json

# parse fetched message data
def parse(data):
    
    total_unread = data['inbox']['summary']['unread_count']
    total_unseen = data['inbox']['summary']['unseen_count']

    packet = "\n###############################################\n\n"
    packet += "no. of People who messaged me: " + str(total_unseen)

    user = 0
    while total_unseen > 0:
        
        packet += "\n\n-------------------------------------------------------------------------------\n\n"

        unread = data['inbox']['data'][user]['unread']
        unseen = data['inbox']['data'][user]['unseen']
        
        if unread:
            packet += "From: " + str( data['inbox']['data'][user]['comments']['data'][-1]['from']['name'] )
            for i in range(-unread,0):
                packet += "\n"+str( data['inbox']['data'][user]['comments']['data'][i]['message'] )

        user += 1
        total_unseen -= unseen
        
    
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