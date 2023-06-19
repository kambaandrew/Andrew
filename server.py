# import all the neccessary modules 
from tkinter import *
from socket import *
import _thread

# Initialize server connection
def initialize_server():
    # initialize socket
    s = socket(AF_INET, SOCK_STREAM)
    # Configure details of the server
    host ='localhost' # to use between devices in the same network e.g 192.168.1.5
    port = 1234
    # initialize server
    s.bind((host, port))
    # set number of clients
    s.listen(1)
    # Accept the connection from the client
    conn, addr = s.accept()
    return conn
# update the chat log
def update_chat(msg, state):
    global chatlog
    chatlog.config(state=NORMAL)
    # update the message in the window
    if state == 0:
        chatlog.insert(END, 'You: '+msg)
    else:
        chatlog.insert(END, 'Other: '+msg)
        chatlog.config(state = DISABLED)
        # show the latest message
        chatlog.yview(END)

#function to send message
def send():
        
    global textbox
    # get the message 
    msg = textbox.get("0.0", END)
    #update the chatlog
    update_chat(msg, 0)
    # send the message
    conn.send(msg.encode('ascii'))
    textbox.delete("0.0", END)
# GUI function definition
# message to receive message
def receive():
    while 1:
        try:
            data = conn.recv(1024)
            msg = data.decode('ascii')
            if msg != "":
                update_chat(msg, 1)
        except:
            pass
def press(event):
    send()
def GUI():
    global chatlog
    global textbox
    # Initialize tkinker object
    gui= Tk()
    # Set title for the chat window
    gui.title("Server chat")
    # Set size for the chat window
    gui.geometry("380x430")
    # text space to display chat messages
    chatlog = Text(gui, bg='white')
    chatlog.config(state=DISABLED) 
    # Button to send chat messages
    sendbutton = Button(gui, bg='orange',fg='red', text='SEND', command= send)
    # Text box to type in the chat messages
    textbox = Text(gui, bg='white')
    # Place the components in the chat window
    chatlog.place(x=6,y=6, height=386, width=370)
    textbox.place(x=6, y=401, height=20, width=265)
    sendbutton.place(x=300, y=401,height=20, width=50)
    # bind textbox to use ENTER key
    textbox.bind("<KeyRelease - Return>", press)
    # create thread to capture message contineously
    _thread.start_new_thread(receive, ())
    # To keep the window in the loop
    gui.mainloop()
if __name__ == '__main__':
    chatlog = textbox = None
    conn = initialize_server()
    GUI()
