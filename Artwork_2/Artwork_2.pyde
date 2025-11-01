# set the size of the canvas
size(700, 700)

# set background colour 
background(140, 99, 138)

class Art: 
    
    def left_black_shape(self): 
        # first black shape
        fill(27, 19, 10)
        stroke(27, 19, 10)
        beginShape()
        vertex(250, 77)
        bezierVertex(210, 12, 80, 5, 40, 90)
        bezierVertex(-12, 170, 10, 240, 45, 335)
        bezierVertex(110, 480, 70, 635, 8, 680)
        bezierVertex(75, 685, 200, 610, 220, 598)
        bezierVertex(210, 590, 200, 570, 194, 557)
        vertex(290, 375)
        vertex(260, 320)
        vertex(222, 290)
        vertex(200, 270)
        vertex(195, 235)
        vertex(250, 78)
        endShape(CLOSE)
        
    def top_right_black_shape(self):
        # top right black shape
        fill(27, 19, 10)
        stroke(27, 19, 10)
        beginShape()
        vertex(570, 210)
        vertex(315, 155)
        vertex(265, 155)
        vertex(250, 77)
        bezierVertex(258, 68, 330, 30, 400, 30)
        bezierVertex(510, -10, 670, 20, 675, 140)
        bezierVertex(680, 250, 580, 230, 570, 210)
        endShape(CLOSE)
        
    def bottom_right_black_shape(self):
        # bottom right black shape
        fill(27, 19, 10)
        stroke(27, 19, 10)
        beginShape()
        vertex(545, 290)
        bezierVertex(610, 290, 655, 330, 660, 375)
        bezierVertex(665, 415, 625, 445, 582.5, 405)
        bezierVertex(547, 377, 505, 390, 500, 420)
        bezierVertex(505, 490, 565, 500, 615, 510)
        bezierVertex(715, 550, 695, 645, 638, 670)
        bezierVertex(570, 675, 455, 650, 420, 585)
        vertex(430, 390)
        vertex(455, 365.5)
        vertex(516.9, 375.5)
        vertex(523, 305)
        endShape(CLOSE)
        
    def first_white_shape(self):
        # first white shape
        fill(234, 209, 174)
        stroke(234, 209, 174)
        beginShape()
        vertex(250, 77)
        bezierVertex(264, 94, 290, 195, 195, 235)
        bezierVertex(180, 195, 193, 125, 250, 77)
        endShape(CLOSE)
        
    def second_white_shape(self):
        # second white shape
        fill(234, 209, 174)
        stroke(234, 209, 174)
        beginShape()
        vertex(195, 235)
        bezierVertex(95, 255, 80, 300, 70, 335)
        bezierVertex(75, 405, 155, 390, 170, 350)
        bezierVertex(195, 290, 225, 295, 222, 290)
        bezierVertex(215, 285, 195, 245, 195, 235)
        endShape(CLOSE)
    
    def third_white_shape(self):
        # third white shape
        fill(218, 194, 166)
        stroke(218, 194, 166)
        beginShape()
        vertex(222, 290)
        bezierVertex(250, 320, 275, 350, 290, 375)
        bezierVertex(300, 340, 280, 280, 222, 290)
        endShape(CLOSE)
        
    def fourth_white_shape(self):
        # fourth white shape
        fill(234, 209, 174)
        stroke(234, 209, 174)
        beginShape()
        vertex(290, 375)
        bezierVertex(250, 430, 230, 420, 205, 450)
        bezierVertex(207, 450, 170, 495, 195, 557)
        vertex(255, 573)
        bezierVertex(320, 520, 340, 450, 290, 375)
        endShape(CLOSE)
        
    def fifth_white_shape(self):
        # fifth white shape
        fill(215, 194, 161)
        stroke(215, 194, 161)
        beginShape()
        vertex(255, 573)
        bezierVertex(250, 578, 235, 590, 220, 599)
        bezierVertex(260, 658, 365, 663, 405, 610)
        endShape(CLOSE)
        
    def sixth_white_shape(self):
        # sixth white shape
        fill(212, 188, 159)
        stroke(212, 188, 159)
        beginShape()
        vertex(420, 585)
        bezierVertex(380, 540, 380, 440, 430, 390)
        bezierVertex(470, 450, 460, 540, 420, 585)
        endShape(CLOSE)
        
    def seventh_white_shape(self):
        # seventh white shape
        fill(208, 185, 154)
        stroke(208, 185, 154)
        beginShape()
        vertex(430, 390)
        bezierVertex(315, 250, 250, 140, 400, 30)
        bezierVertex(590, 70, 590, 220, 545, 290)
        bezierVertex(525, 325, 450, 360, 430, 390)
        endShape(CLOSE)
        
    def black_circle(self):
        # black circle
        fill(27, 19, 10)
        stroke(27, 19, 10)
        beginShape()
        vertex(570, 210)
        bezierVertex(515, 152, 455, 152, 425, 207.5)
        bezierVertex(415, 305, 500, 305, 545, 290)
        bezierVertex(565, 260, 570, 220, 570, 210)
        endShape(CLOSE)
        
    def white_triangle(self):
        # white triangle
        fill(234, 209, 174)
        stroke(234, 209, 174)
        beginShape()
        vertex(405, 610)
        bezierVertex(403, 615, 425, 580, 420, 585)
        bezierVertex(422, 590, 434, 610, 447, 619)
        endShape(CLOSE)
        
    def left_transparent_shape(self):
        # left transparent shape 
        fill(153, 60, 76, 150)
        stroke(153, 60, 76, 30)
        beginShape()
        vertex(4, 3)
        vertex(145, 350)
        vertex(159, 270)
        vertex(286, 280)
        vertex(230, 156)
        vertex(525, 156)
        endShape(CLOSE)
        
    def right_transparent_shape(self):    
        # right transparent shape 
        fill(153, 60, 76, 150)
        stroke(153, 60, 76, 30)
        beginShape()
        vertex(682, 691)
        vertex(638, 674)
        bezierVertex(615, 664, 455, 618, 447, 620.2)
        vertex(125, 542)
        vertex(415, 492.5)
        vertex(325, 342)
        vertex(516, 375)
        vertex(529, 248)
        endShape(CLOSE)
        
art = Art()
art.left_black_shape()
art.top_right_black_shape()
art.bottom_right_black_shape()
art.first_white_shape()
art.second_white_shape()
art.third_white_shape()
art.fourth_white_shape()
art.fifth_white_shape()
art.sixth_white_shape()
art.seventh_white_shape()
art.black_circle()
art.white_triangle()
art.left_transparent_shape()
art.right_transparent_shape()
