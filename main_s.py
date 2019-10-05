import comm_s


#1 Join the master - Login
#2 Recieve the command
#3 Execute the command
#4 Return the Result to the Master
#5 Log out


#1 Join the master - Login
port = comm_s.send_message_to_master()
#Checking back
comm_s.listen_to_master(port)