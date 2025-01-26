m = 0


import tkinter
from tkinter import messagebox
from tkinter import PhotoImage

base = tkinter.Tk()
base.title('PvP Chess')
base.geometry('520x520')


wpawn = PhotoImage(file = 'white pawn.gif')
bpawn = PhotoImage(file = 'black pawn.gif')
whorse = PhotoImage(file = 'white horse.gif')
bhorse = PhotoImage(file = 'black horse.gif')
wrook = PhotoImage(file = 'white rook.gif')
brook = PhotoImage(file = 'black rook.gif')
wbishop = PhotoImage(file = 'white bishop.gif')
bbishop = PhotoImage(file = 'black bishop.gif')
wking = PhotoImage(file = 'white king.gif')
bking = PhotoImage(file = 'black king.gif')
wqueen = PhotoImage(file = 'white queen.gif')
bqueen = PhotoImage(file = 'black queen.gif')




c =52
k =60

board = tkinter.Canvas (base, width =c*9, height =c*9)
board.place(x =k, y =k)


#img = PhotoImage(file = 'Chess Board.gif')
#board.create_image(0, 0,anchor ='nw', image =img)

board.create_rectangle(0, 0, c*8, c*8, fill ='white')
board.create_line(4, 0, 4, c*8+2, width =4, fill ='green')
board.create_line(4, c*8, c*8+2, c*8, width =4, fill ='green')
board.create_line(c*8, c*8, c*8, 2, width =4, fill ='green')
board.create_line(c*8, 4, 0, 4, width =4, fill ='green')

for n in range(1, 8):
    board.create_line(c*n, 0, c*n, c*8, width =2, fill ='green')
    board.create_line(0, c*n, c*8, c*n, width =2, fill ='green')



#this cursor will go to all available moves of a clicked piece
cursor1 = board.create_image(510, 510)


object_id_of_1st_black_piece = board.create_image(6, 6, image =brook, anchor ='nw')
board.create_image(c+6, 6, image =bhorse, anchor ='nw')
board.create_image(c*2+6, 6, image =bbishop, anchor ='nw')
board.create_image(c*3+6, 6, image =bqueen, anchor ='nw')
board.create_image(c*4+6, 6, image =bking, anchor ='nw')
board.create_image(c*5+6, 6, image =bbishop, anchor ='nw')
board.create_image(c*6+6, 6, image =bhorse, anchor ='nw')
board.create_image(c*7+6, 6, image =brook, anchor ='nw')
for i in range(8):
    board.create_image(c*i+6, c+6, image =bpawn, anchor ='nw')

object_id_of_1st_white_piece = board.create_image(6, c*7+6, image =wrook, anchor ='nw')
board.create_image(c+6, c*7+6, image =whorse, anchor ='nw')
board.create_image(c*2+6, c*7+6, image =wbishop, anchor ='nw')
board.create_image(c*3+6, c*7+6, image =wqueen, anchor ='nw')
board.create_image(c*4+6, c*7+6, image =wking, anchor ='nw')
board.create_image(c*5+6, c*7+6, image =wbishop, anchor ='nw')
board.create_image(c*6+6, c*7+6, image =whorse, anchor ='nw')
board.create_image(c*7+6, c*7+6, image =wrook, anchor ='nw')

for i in range(8):
    board.create_image(c*i+6, c*6+6, image =wpawn, anchor ='nw')


board.addtag_enclosed('white', 0, c*6, c*8, c*8)
board.addtag_enclosed('black', 0, 0, c*8, c*2)


board.dtag(5, 'black')
board.dtag(7, 'black')
board.dtag(19, 'white')
#print (board.gettags(21))
#print (board.find_withtag('black'))
#print (board.coords(21))
#print (board.coords(22))
#print(board.find_withtag('white'))




def check_the_places_of_lowly_soliders_and_the_state_of_kings():
    for i in range(b_id+8, b_id+16):
        if len(board.find_withtag(i)) > 0:
            k  = board.coords(i)
            if k[1] == 6+c*7:
                board.delete(i)
                board.create_image(k[0], k[1], image =bqueen, anchor ='nw',
                                    tags = ('black', 'black solider-turned-minister'))
                break
    for i in range(w_id+8, w_id+16):
        if len(board.find_withtag(i)) > 0:
            k  = board.coords(i)
            if k[1] == 6:
                board.delete(i)
                board.create_image(k[0], k[1], image =wqueen, anchor ='nw',
                                    tags = ('white', 'white solider-turned-minister'))
                break
    global m
    if len(board.find_withtag(w_id+4)) < 1:
            note = messagebox.askquestion('Game Over',
                              'The white king has been destroyed. Continue playing around anyway?')
            if note == 'no':
                                base.destroy()
            else:                   m+=1
    if len(board.find_withtag(b_id+4)) < 1:
        if m < 1:
            
            note = messagebox.askquestion('Game Over',
                              'The black king has been destroyed. Continue playing around anyway?')
            if note == 'no':
                                base.destroy()
            else:               m+=1



print("right click only tells you the widgets occupyng the clicked panel")
print("the widget with id 1 is the background white rectangle")
def right_click(event):
    for j in range(6, c*8+6, c):
        for i in range(6, c*8+6, c):
            if i+1 < event.x < i+c-10 and j+1 < event.y < j+c-10:
                found = event.widget.find_overlapping(i+1, j+20,
                                                          i+20, j+20)
                print (found, 'in panel ', i, j)
                break
board.bind("<Button-3>", right_click)





b_id =object_id_of_1st_black_piece
w_id =object_id_of_1st_white_piece

def black_piece_clicked (event):
    global piece_waiting_to_move
    remaining_black_pieces = board.find_withtag('black')
    for i in remaining_black_pieces:
        if (c-10+int(board.coords(i)[0]) > event.x > 1+int(board.coords(i)[0])):
            if (c-9+int(board.coords(i)[1]) > event.y > 1+int(board.coords(i)[1])):
                if b_id+8 <= i < b_id+16:
                    bpawn_move(i)
                elif i == b_id or i == b_id+7:
                    rook_move(i)
                elif i == b_id+1 or i == b_id+6:
                    horse_move(i)
                elif i == b_id+2 or i == b_id+5:
                    elephant_move(i)
                elif i == b_id+3 or i in board.find_withtag("black solider-turned-minister"):
                    queen_move(i)
                elif i == b_id+4:
                    king_move(i)
                
                
                if len(board.find_withtag('allowed')) > 0:
                    board.bind('<Button-1>', panel_click)
                    piece_waiting_to_move = i
                else:
                    messagebox.showinfo('', "no available moves")
                break


def white_piece_clicked (event):
    global piece_waiting_to_move
    remaining_white_pieces = board.find_withtag("white")
    for i in remaining_white_pieces:
        if (c-10+int(board.coords(i)[0]) > event.x > 1+int(board.coords(i)[0])):
            if (c-9+int(board.coords(i)[1]) > event.y > 1+int(board.coords(i)[1])):
                if w_id+8 <= i < w_id+16:
                    wpawn_move(i)
                elif i == w_id or i == w_id+7:
                    rook_move(i)
                elif i == w_id+1 or i == w_id+6:
                    horse_move(i)
                elif i == w_id+2 or i == w_id+5:
                    elephant_move(i)
                elif i == w_id+3 or i in board.find_withtag("white solider-turned-minister"):
                    queen_move(i)
                elif i == w_id+4:
                    king_move(i)

                
                if len(board.find_withtag('allowed')) > 0:
                    board.bind('<Button-1>', panel_click)
                    piece_waiting_to_move = i
                else:
                    messagebox.showinfo('', "no available moves")
                break

global ally, enemy
ally = 'white'
enemy = 'black'
board.bind('<Button-1>', white_piece_clicked)

#board.tag_raise(1)


for j in range(c*2+6, c*6+6, c):
    for i in range(6, c*8+6, c):
        board.create_rectangle(i+1, j+1, i+c-10, j+c-9, fill='',
                               tags ='empty', outline ='')

#print(board.find_withtag('empty'))




def allow (a, b):
    i = board.create_rectangle(a+1, b+1, a+c-10, b+c-9, fill='', outline ='blue',
                           tags ='allowed', width =3)
    

#cursor2 will scout ahead so that cursor1 never goes out of bounds
cursor2 = board.create_image(510, 510)


def remove_enemy_piece(x, y):
    #print (ally)
    enemy_piece_id =board.find_closest(x+20, y+20)
    if enemy in board.gettags(enemy_piece_id):
        board.delete(enemy_piece_id)
    else: print("Error. Attempting to delete nonexistent enemy")
    

def allowed_panel(x, y):
    stuff = board.find_overlapping(x+1, y+20, x+20, y+20)
    for i in stuff:
        if 'allowed' in board.gettags(i):
            return True
    return False


#allow(6+c*4,6+c*4)
#print (allowed_panel(c*5+6, c*4+6))
#print (allowed_panel(6+c*4,6+c*4))

    


def empty_panel(x, y):
    stuff = board.find_overlapping(x+1, y+20, x+20, y+20)
    for i in stuff:
        if 'empty' in board.gettags(i):
            return (True, i)
    return (False, 0)



def next_turn(friend):
    #the following global is important. Please do not remove it.
    global ally, enemy
    ally = friend
    if ally == 'white':
        board.bind("<Button-1>", black_piece_clicked)
        ally = 'black'
        enemy = 'white'
        print ("black's turn")
    elif ally == 'black':
        board.bind('<Button-1>', white_piece_clicked)
        ally = 'white'
        enemy = 'black'
        print("white's turn")
    else:
        print("a third party has joined the fray lol")

def same_turn(ally):
    if ally == 'white':
        board.bind('<Button-1>', white_piece_clicked)
        print("still white's turn")
    elif ally == 'black':
        board.bind('<Button-1>', black_piece_clicked)
        print("still black's turn")
    else:
        print("a third party has joined the fray lol")





def panel_click(event):#a very complicated function
    global m
    piece_id = piece_waiting_to_move
    x = board.coords(piece_id)
    for i in range(6, c*8+6, c):
        for j in range(6, c*8+6, c):
            if i+1 < event.x < i+c-10 and j+1 < event.y < j+c-10:
                occupying = event.widget.find_overlapping(i+1, j+20,
                                                          i+20, j+20)
                #print('occupying      ', occupying)
                k = empty_panel(i, j)
                #print('empty panel', k)
                if allowed_panel(i, j):
                    if k[0]:
                        board.coords(k[1],x[0]+1, x[1]+1,x[0]+c-10, x[1]+c-9)
                        board.coords(piece_id, i, j)
                        next_turn(ally)
                        break
                    else:
                        remove_enemy_piece(i, j)
                        board.coords(piece_id, i, j)
                        board.create_rectangle(x[0]+1, x[1]+1, x[0]+c-10,x[1]+c-9,
                                               fill='',tags ='empty', outline ='')
                        next_turn(ally)
                        break
                else:
                    same_turn(ally)
                    break
    board.delete('allowed')
    if m != 1:
        check_the_places_of_lowly_soliders_and_the_state_of_kings()
    if ally == 'white':
        board.bind('<Button-1>', white_piece_clicked)
    else:
        board.bind('<Button-1>', black_piece_clicked)



#print(board.find_overlapping(c*7+26, c*5+26, c*7+26, c*5+26))
#print(board.find_overlapping(26, c*2+26, 26, c*2+26))




def initialize_cursors(piece_id):
    board.coords(cursor1, board.coords(piece_id))
    board.coords(cursor2, board.coords(piece_id))


def check_up():
    #checks the panel one step above the current panel
    board.move(cursor2, 0, -c)
    if board.coords(cursor2)[1] < 0:
        return 'boundary'
    else:
        p = [int(i+20) for i in board.coords(cursor2)]
        r = board.find_overlapping(p[0], p[1], p[0], p[1])
        #print (p, r)
        if 'empty' in board.gettags(r[1]):
            return 'empty'
        elif 'black' in board.gettags(r[1]):
            return 'black'
        elif 'white' in board.gettags(r[1]):
            return 'white'

def check_down():
    board.move(cursor2, 0, c)
    if board.coords(cursor2)[1] > c*8:
        return 'boundary'
    else:
        p = [int(i+20) for i in board.coords(cursor2)]
        r = board.find_overlapping(p[0], p[1], p[0], p[1])
        if 'empty' in board.gettags(r[1]):
            return 'empty'
        elif 'black' in board.gettags(r[1]):
            return 'black'
        elif 'white' in board.gettags(r[1]):
            return 'white'

def check_left():
    board.move(cursor2, -c, 0)
    if board.coords(cursor2)[0] < 0:
        return 'boundary'
    else:
        p = [int(i+20) for i in board.coords(cursor2)]
        r = board.find_overlapping(p[0], p[1], p[0], p[1])
        #print(r)
        if 'empty' in board.gettags(r[1]):
            return 'empty'
        elif 'black' in board.gettags(r[1]):
            return 'black'
        elif 'white' in board.gettags(r[1]):
            return 'white'

def check_right():
    board.move(cursor2, c, 0)
    if board.coords(cursor2)[0] > c*8:
        return 'boundary'
    else:
        p = [int(i+20) for i in board.coords(cursor2)]
        r = board.find_overlapping(p[0], p[1], p[0], p[1])
        #print(r)
        if 'empty' in board.gettags(r[1]):
            return 'empty'
        elif 'black' in board.gettags(r[1]):
            return 'black'
        elif 'white' in board.gettags(r[1]):
            return 'white'






def move_up(piece_id):
    s = check_up()
    if s == 'boundary':
        initialize_cursors(piece_id)
    elif ally != s :
            board.move(cursor1, 0, -c)
            p = board.coords(cursor1)
            allow(p[0], p[1])
            initialize_cursors(piece_id)
    else: initialize_cursors(piece_id)

def move_down(piece_id):
    s = check_down()
    if s == 'boundary':
        initialize_cursors(piece_id)
    elif ally != s :
            board.move(cursor1, 0, c)
            p = board.coords(cursor1)
            allow(p[0], p[1])
            initialize_cursors(piece_id)
    else: initialize_cursors(piece_id)


def move_left(piece_id):
    s = check_left()
    if s == 'boundary':
        initialize_cursors(piece_id)
    elif ally != s :
            board.move(cursor1, -c, 0)
            p = board.coords(cursor1)
            allow(p[0], p[1])
            initialize_cursors(piece_id)
    else: initialize_cursors(piece_id)


def move_right(piece_id):
    s = check_right()
    if s == 'boundary':
        initialize_cursors(piece_id)
    elif ally != s :
            board.move(cursor1, c, 0)
            p = board.coords(cursor1)
            allow(p[0], p[1])
            initialize_cursors(piece_id)
    else: initialize_cursors(piece_id)





def jump_up(piece_id):
    s = check_up()
    if s == 'boundary':
        initialize_cursors(piece_id)
        return False
    else:
        board.move(cursor1, 0, -c)
        return True
def jump_down(piece_id):
    s = check_down()
    if s == 'boundary':
        initialize_cursors(piece_id)
        return False
    else:
        board.move(cursor1, 0, c)
        return True
def jump_left(piece_id):
    s = check_left()
    if s == 'boundary':
        initialize_cursors(piece_id)
        return False
    else:
        board.move(cursor1, -c, 0)
        return True
def jump_right(piece_id):
    s = check_right()
    if s == 'boundary':
        initialize_cursors(piece_id)
        return False
    else:
        board.move(cursor1, c, 0)
        return True










def wpawn_move(piece_id):
    initialize_cursors(piece_id)
    s = check_up()
    if s == 'empty':
        check_down()#for counter-balance
        move_up(piece_id)
    else:
        initialize_cursors(piece_id)
    if jump_up(piece_id):
        s = check_left()
        if s == enemy:
            check_right()#for counter-balance
            move_left(piece_id)
        else:
            initialize_cursors(piece_id)
    if jump_up(piece_id):
        s = check_right()
        if s == enemy:
            check_left()#for counter-balance
            move_right(piece_id)
        else:
            initialize_cursors(piece_id)


def bpawn_move(piece_id):
    initialize_cursors(piece_id)
    s = check_down()
    if s == 'empty':
        check_up()#for counter-balance
        move_down(piece_id)
    else:
        initialize_cursors(piece_id)
    if jump_down(piece_id):
        s = check_left()
        if s == enemy:
            check_right()#for counter-balance
            move_left(piece_id)
        else:
            initialize_cursors(piece_id)
    if jump_down(piece_id):
        s = check_right()
        if s == enemy:
            check_left()#for counter-balance
            move_right(piece_id)
        else:
            initialize_cursors(piece_id)


def horse_move(piece_id):
    initialize_cursors(piece_id)
    if jump_up(piece_id):
        if jump_up(piece_id):
            move_left(piece_id)
    if jump_up(piece_id):
        if jump_up(piece_id):
            move_right(piece_id)
            
    if jump_down(piece_id):
        if jump_down(piece_id):
            move_left(piece_id)
    if jump_down(piece_id):
        if jump_down(piece_id):
            move_right(piece_id)
            
    if jump_left(piece_id):
        if jump_left(piece_id):
            move_up(piece_id)
    if jump_left(piece_id):
        if jump_left(piece_id):
            move_down(piece_id)
            
    if jump_right(piece_id):
        if jump_right(piece_id):
            move_up(piece_id)
    if jump_right(piece_id):
        if jump_right(piece_id):
            move_down(piece_id)
    
    
def rook_move(piece_id):
    initialize_cursors(piece_id)
    n = 0
    while True :
        for i in range(n):
            if n == 0:
                break
            jump_up(piece_id)
        s = check_up()
        check_down() #for counterbalancing cursor2
        if s == 'boundary' or s == ally:
            break
        elif s == enemy:
            move_up(piece_id)
            break
        else:
            move_up(piece_id)
            n+=1
    initialize_cursors(piece_id)
    n = 0
    while True :
        for i in range(n):
            if n == 0:
                break
            jump_down(piece_id)
        s = check_down()
        check_up() #for counterbalancing cursor2
        if s == 'boundary' or s == ally:
            break
        elif s == enemy:
            move_down(piece_id)
            break
        else:
            move_down(piece_id)
            n+=1
    initialize_cursors(piece_id)
    n = 0
    while True :
        for i in range(n):
            if n == 0:
                break
            jump_left(piece_id)
        s = check_left()
        check_right() #for counterbalancing cursor2
        if s == 'boundary' or s == ally:
            break
        elif s == enemy:
            move_left(piece_id)
            break
        else:
            move_left(piece_id)
            n+=1
    initialize_cursors(piece_id)
    n = 0
    while True :
        for i in range(n):
            if n == 0:
                break
            jump_right(piece_id)
        s = check_right()
        check_left() #for counterbalancing cursor2
        if s == 'boundary' or s == ally:
            break
        elif s == enemy:
            move_right(piece_id)
            break
        else:
            move_right(piece_id)
            n+=1



def elephant_move(piece_id):
    initialize_cursors(piece_id)
    n = 0
    while True:
        if not jump_up(piece_id):
            break
        for i in range(n):
            jump_up(piece_id)
            jump_left(piece_id)
        s = check_left()
        check_right()
        if s == ally or s == 'boundary':
            break
        elif s == enemy:
            move_left(piece_id)
            break
        else:
            k = check_up()
            check_down()
            move_left(piece_id)
            if k == 'boundary':
                break
            n+=1
    initialize_cursors(piece_id)
    n = 0
    while True:
        if not jump_up(piece_id):
            break
        for i in range(n):
            jump_up(piece_id)
            jump_right(piece_id)
        s = check_right()
        check_left()
        if s == ally or s == 'boundary':
            break
        elif s == enemy:
            move_right(piece_id)
            break
        else:
            k = check_up()
            check_down()
            move_right(piece_id)
            if k == 'boundary':
                break
            n+=1
    initialize_cursors(piece_id)
    n = 0
    while True:
        if not jump_down(piece_id):
            break
        #print(board.coords(cursor1))
        for i in range(n):
            jump_down(piece_id)
            jump_left(piece_id)
        s = check_left()
        check_right()
        #print (board.coords(cursor1))
        #print(s)
        if s == ally or s == 'boundary':
            break
        elif s == enemy:
            move_left(piece_id)
            break
        else:
            k = check_down()
            check_up()
            #print(k)
            move_left(piece_id)
            if k == 'boundary':
                break
            n+=1
    initialize_cursors(piece_id)
    n = 0
    while True:
        if not jump_down(piece_id):
            break
        for i in range(n):
            jump_down(piece_id)
            jump_right(piece_id)
        s = check_right()
        check_left()
        if s == ally or s == 'boundary':
            break
        elif s == enemy:
            move_right(piece_id)
            break
        else:
            k = check_down()
            check_up()
            move_right(piece_id)
            if k == 'boundary':
                break
            n+=1



def queen_move(piece_id):
    rook_move(piece_id)
    elephant_move(piece_id)



def king_move(piece_id):
    initialize_cursors(piece_id)
    move_up(piece_id)
    move_down(piece_id)
    move_left(piece_id)
    move_right(piece_id)
    if jump_up(piece_id):
        move_left(piece_id)
    if jump_up(piece_id):
        move_right(piece_id)
    if jump_down(piece_id):
        move_left(piece_id)
        if jump_down(piece_id):
            move_right(piece_id)



#print(board.find_overlapping(c+26, 26, c+26, 26)[1])
#print(i +23 for i in board.coords(28))
#print ( 'black' in board.gettags(22))
#print(board.find_overlapping(8+c*4, 26+c*4, 26+c*4, 26+c*4)) 
#board.delete(40)
#newone = board.create_line(511,511,511,511, fill='')
#print (newone)    


base.mainloop()


