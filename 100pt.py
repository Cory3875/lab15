#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=0)
		
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "blue")
		self.down.grid(row=0,column=1)			
		
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "red")
		self.left.grid(row=0,column=2)
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "yellow")
		self.right.grid(row=0,column=3)
		
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
                self.down.bind("<Button-1>", self.movedown)
                self.right.bind("<Button-1>", self.moveright)
		self.left.bind("<Button-1>", self.moveleft)  
		
		
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
		global drawpadwidth
		global drawpadheight
                x1,y1,x2,y2 = drawpad.coords(player)
                if y1 <= 13:
                    drawpad.move(player,0,0)
                else:
                    drawpad.move(player,0,-10)
    
        def movedown(self, event):   
		global player
		global drawpad
                global drawpadwidth
		global drawpadheight
                x1,y1,x2,y2 = drawpad.coords(player)
                if y2 >= 320:
                    drawpad.move(player,0,0)
                else:
                    drawpad.move(player,0,10)
    
        
        def moveright(self, event):   
		global player
		global drawpad
                global drawpadwidth
		global drawpadheight
                x1,y1,x2,y2 = drawpad.coords(player)
                if x2 >= 480:
                    drawpad.move(player,0,0)
                else:
                    drawpad.move(player,10,0)
    
        
        def moveleft(self, event):   
		global player
		global drawpad
                global drawpadwidth
		global drawpadheight
                x1,y1,x2,y2 = drawpad.coords(player)
                if x1 <= 10:
                    drawpad.move(player,0,0)
                else:
                    drawpad.move(player,-10,0)
    
        
        
        
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    global drawpad
	    # Insert the code here to make the target move, bouncing on the edges    
	    targetx1,targety1,targetx2,targety2 = drawpad.coords(target)   
	    if targetx2 >= 480:
	        direction = -4    
            if targetx1 <= 0:
                direction = 4
            drawpad.move(target,direction,0)
          

            
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            if didWeHit == True:
                drawpad.move(target,0,0)
                drawpad.itemconfig(target, fill='blue')
            else:
                drawpad.itemconfig(target, fill='red')
                drawpad.after(10,self.animate)
                
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                global didWeHit
                global target, targetx1, targety1, targetx2, targety2
                targetx1, targety1, targetx2, targety2 = drawpad.coords(target)
                x1,y1,x2,y2 = drawpad.coords(player)
                if x1 >= targetx1 and x2 <= targetx2 and y1 >= targety1 and y2 <= targety2:
                    return True
                
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)
                
                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)

root.mainloop()