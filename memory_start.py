from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os, random, time

top_list = []
bottom_list = []
list_of_top_cards = []
list_of_bottom_cards = []

click_one = None
click_two = None
previous_card = None
able = True
score = 0
time_taken = [0,0,0]
count = 0
done = 0

win = Tk()

list_of_images = []
back_image = Image.open('Media/back.png')
back_img = ImageTk.PhotoImage(back_image)

for i in range(1,15):
	im = Image.open(f'Media/{str(i)}.png')
	list_of_images.append(im)

while len(top_list) <= 13:
	num = random.randint(1,14)
	if num not in top_list:
		top_list.append(num)

while len(bottom_list) <= 13:
	num = random.randint(1,14)
	if num not in bottom_list:
		bottom_list.append(num)

def set_able():
	global able
	able = True

def set_time():
	global count, time_taken
	count += 1
	time_taken[2] = count

	if count > 59:
		if int(time_taken[1]) >= 59:
			time_taken[1] = 0
		else:
			time_taken[1] = int(int(time_taken[1])+1)
		count = 0

	if len(str(time_taken[0])) == 1:
		time_taken[0] = f'0{time_taken[0]}'
	if len(str(time_taken[1])) == 1:
		time_taken[1] = f'0{time_taken[1]}'
	if len(str(time_taken[2])) == 1:
		time_taken[2] = f'0{time_taken[2]}'

	label_time.config(text=f'{time_taken[0]} : {time_taken[1]} : {time_taken[2]}')
	label_time.text= f'{time_taken[0]} : {time_taken[1]} : {time_taken[2]}'

	win.after(1000, set_time)

def set_score():
	global score
	label_score.config(text=f'Score : {score}')
	label_score.text = f'Score : {score}'

def turn_back(w1,w2):
	w1.widget.config(image=back_img)
	w2.widget.config(image=back_img)

	previous_card = None

	set_able()

def get_num(event):
	global click_one, click_two, previous_card, able, score, done, time_taken

	if able == True:
		nimg = list_of_images[int(event.widget.id)-1]
		nimage = ImageTk.PhotoImage(nimg)

		event.widget.config(image=nimage)
		event.widget.image = nimage

		if click_one == None:
			click_one = int(event.widget.id)
			previous_card = event
		else:
			click_two = int(event.widget.id)
			able = False

		if click_two != None:
			if click_one == click_two:
				print('bingo you got it')
				score += 100
				done += 1

				if done >= 13:
					messagebox.showinfo('Winner',f'You Win The Game in {time_taken}, and your score is {score}')

				previous_card = None
				click_one = None
				click_two = None
				set_able()
				set_score()
			else:
				click_one = None
				click_two = None

				win.after(1000,lambda : turn_back(event,previous_card))

frame_ui = Frame(win)
frame_ui.pack(side='top',expand=True,fill=X) 

label_time = Label(frame_ui,text=f'{time_taken[0]} : {time_taken[1]} : {time_taken[2]}',font=('arial',15))
label_time.pack(side='left',anchor='nw',padx=10)

label_score = Label(frame_ui,text=f'Score : {score}',font=('arial',15))
label_score.pack(side='right',padx=10)


fr_top = Frame(win)
fr_top.pack(padx=5,pady=5)

fr_top_one = Frame(fr_top)
fr_top_one.pack()

fr_top_two = Frame(fr_top)
fr_top_two.pack()

sep = ttk.Separator(win,orient=HORIZONTAL)
sep.pack(expand=True,fill=X,padx=10,pady=10)

fr_bottom = Frame(win)
fr_bottom.pack(padx=5,pady=5)

fr_bottom_one = Frame(fr_bottom)
fr_bottom_one.pack()

fr_bottom_two = Frame(fr_bottom)
fr_bottom_two.pack()

for i in top_list:
	if int(i) <= 7:
		im = Image.open(f'Media/{str(i)}.png')
		img = ImageTk.PhotoImage(im)

		l = Label(fr_top_one,image=back_img)
		l.config(image=back_img)
		l.image = back_img
		l.id = int(i)
		l.bind('<Button-1>',get_num)
		l.pack(side='left')
		list_of_top_cards.append(l)
	else:
		im = Image.open(f'Media/{str(i)}.png')
		img = ImageTk.PhotoImage(im)

		l = Label(fr_top_two,image=back_img)
		l.config(image=back_img)
		l.image = back_img
		l.id = int(i)
		l.bind('<Button-1>',get_num)
		l.pack(side='left')
		list_of_top_cards.append(l)


for i in bottom_list:
	if int(i) <= 7:
		im = Image.open(f'Media/{str(i)}.png')
		img = ImageTk.PhotoImage(im)

		l = Label(fr_bottom_one,image=back_img)
		l.config(image=back_img)
		l.image = back_img
		l.id = int(i)
		l.bind('<Button-1>',get_num)
		l.pack(side='left')
		list_of_bottom_cards.append(l)
	else:
		im = Image.open(f'Media/{str(i)}.png')
		img = ImageTk.PhotoImage(im)

		l = Label(fr_bottom_two,image=back_img)
		l.config(image=back_img)
		l.image = back_img
		l.id = int(i)
		l.bind('<Button-1>',get_num)
		l.pack(side='left')
		list_of_bottom_cards.append(l)

win.after(1000, set_time)

win.mainloop()
