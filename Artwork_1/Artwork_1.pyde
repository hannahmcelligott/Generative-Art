# set the size of the canvas 
size(770, 770)

# background colour 
background(242, 242, 242)

# class responsible for creating the artwork
class Art:

    # draw the third red shape 
    def third_red_shape(self):
        # third red shape 
        fill(174, 49, 49)
        stroke(174, 49, 49)
        beginShape()
        vertex(195.1, 497.9)
        vertex(292.6, 497.9)
        vertex(292.6, 574.9)
        vertex(400.4, 574.9)
        vertex(400.4, 626.3)
        vertex(436.3, 626.3)
        vertex(436.3, 770)
        vertex(195.1, 770)
        endShape(CLOSE)

    def first_orange_shape(self):
        # first orange shape 
        fill(224, 105, 43)
        stroke(224, 105, 43)
        beginShape()
        vertex(0, 590.3)
        vertex(51.3, 590.3)
        vertex(195.1, 497.9)
        vertex(195.1, 605.73)
        vertex(282.3, 605.73)
        vertex(282.3, 682.7)
        vertex(385, 682.7)
        vertex(385, 770)
        vertex(0, 770)
        endShape(CLOSE)
        
    def first_red_shape(self):
        # first red shape 
        fill(174, 49, 49)
        stroke(174, 49, 49)
        beginShape()
        vertex(0,770)
        vertex(0, 667.3)
        vertex(102.7, 667.3)
        vertex(102.7, 718.7)
        vertex(154, 718.7)
        vertex(154, 770)
        endShape(CLOSE)
        
    def first_yellow_triangle(self):
        # first yellow triangle 
        fill(219, 179, 56)
        stroke(219, 179, 56)
        beginShape()
        vertex(0, 770)
        vertex(51.3, 590.3)
        vertex(195.1, 497.9)
        endShape(CLOSE)
        
    def second_yellow_triangle(self):
        # second yellow triangle 
        fill(219, 179, 56)
        stroke(219, 179, 56)
        beginShape()
        vertex(118.1, 682.7)
        vertex(154, 605.73)
        vertex(154, 682.7)
        endShape(CLOSE)
        
    def third_yellow_triangle(self):
        # third yellow triangle 
        fill(219, 179, 56)
        stroke(219, 179, 56)
        beginShape()
        vertex(154, 770)
        vertex(154, 718.7)
        vertex(205.3, 770)
        endShape(CLOSE)
        
    def last_red_shape(self):
        # last red shape
        fill(174, 49, 49)
        stroke(174, 49, 49)
        beginShape()
        vertex(467.1, 477.4)
        vertex(569.8, 477.4)
        vertex(569.8, 544.1)
        vertex(687.9, 544.1)
        vertex(687.9, 626.3)
        vertex(770, 626.3)
        vertex(770, 770)
        vertex(467.1, 770)
        endShape(CLOSE)
        
    def second_red_shape(self):
        # second red shape
        fill(174, 49, 49)
        stroke(174, 49, 49)
        beginShape()
        vertex(154, 682.7)
        vertex(154, 605.73)
        vertex(195.1, 605.73)
        vertex(195.1, 682.7)
        endShape(CLOSE)
        
    def fifth_yellow_triangle(self):
        # fifth yellow triangle 
        fill(219, 179, 56)
        stroke(219, 179, 56)
        beginShape()
        vertex(385, 682.7)
        vertex(385, 770)
        vertex(436.3, 770)
        endShape(CLOSE)
        
    def sixth_yellow_triangle(self):
        #sixth yellow triangle 
        fill(219, 179, 56)
        stroke(219, 179, 56)
        beginShape()
        vertex(564.7, 590.3)
        vertex(564.7, 713.5)
        vertex(667.3, 713.5)
        endShape(CLOSE)
        
    def last_yellow_triangle(self):
        # last yellow triangle 
        fill(219, 179, 56)
        stroke(219, 179, 56)
        beginShape()
        vertex(718.7, 713.5)
        vertex(718.7, 744.3)
        vertex(764.9, 744.3)
        endShape(CLOSE)
        
    def last_orange_shape(self):
        # last orange shape 
        fill(224, 105, 43)
        stroke(224, 105, 43)
        beginShape()
        vertex(436.3, 770)
        vertex(436.3, 590.3)
        vertex(564.7, 590.3)
        vertex(564.7, 713.5)
        vertex(718.7, 713.5)
        vertex(718.7, 744.3)
        vertex(770, 744.3)
        vertex(770, 770)
        endShape(CLOSE)
        
    def first_yellow_shape(self):
        # first yellow shape 
        fill(219, 179, 56)
        stroke(219, 179, 56)
        beginShape()
        vertex(400.4, 574.9)
        vertex(400.4, 626.3)
        vertex(467.1, 626.3)
        vertex(467.1, 477.4)
        endShape(CLOSE)
        
    def fourth_red_shape(self):
        # fourth red shape 
        fill(174, 49, 49)
        stroke(174, 49, 49)
        beginShape()
        vertex(436.3, 626.3)
        vertex(436.3, 590.3)
        vertex(467.1, 590.3)
        vertex(467.1, 626.3)
        endShape(CLOSE)
        
    def fourth_yellow_triangle(self):
        # fourth yellow triangle 
        fill(219, 179, 56)
        stroke(219, 179, 56)
        beginShape()
        vertex(267, 770)
        vertex(351, 574.9)
        vertex(401.5, 571)
        endShape(CLOSE)
        
    def second_orange_shape(self):
        # second orange shape 
        fill(224, 105, 43)
        stroke(224, 105, 43)
        beginShape()
        vertex(351, 574.9)
        vertex(399.5, 574.9)
        vertex(467, 478.2)
        endShape(CLOSE)
    
    def pale_yellow_fork_triangle(self):
        # pale yellow fork triangle
        fill(225, 197, 84)
        stroke(225, 197, 84)
        beginShape()
        vertex(540, 770)
        vertex(628, 544.1)
        vertex(637, 544.1)
        vertex(623, 635)
        vertex(687.9, 578)
        vertex(687.9, 625)
        endShape(CLOSE)
        
    def navy_semicircle(self):
        # navy semicircle
        fill(51, 52, 90)
        stroke(51, 52, 90)
        bezier(770, 0, 730, 33, 723, 120, 770, 185)
        
    def navy_left_boarder_semicircles(self):
        # navy left boarder semicircles 
        fill(51, 52, 90)
        stroke(51, 52, 90)
        beginShape()
        vertex(0, 420)
        bezierVertex(0, 405, 34, 380, 34, 383)
        bezierVertex(9, 360, 10, 310, 37, 290)
        bezierVertex(20, 270, 15, 220, 33, 185)
        bezierVertex(50, 100, 50, 90, 100, 70)
        bezierVertex(50, 50, 10, 20, 0, 0)
        endShape(CLOSE)
        
    def top_blue_cloud(self):
        # top blue cloud
        fill(64, 96, 165)
        stroke(64, 96, 165)
        beginShape()
        vertex(0, 0)
        bezierVertex(15, 45, 50, 70, 100, 70)
        bezierVertex(3, 80, 15, 160, 33, 185)
        vertex(690, 75)
        bezierVertex(680, 82, 730 , 47, 764, 0)
        line(764, 0, 0, 0)
        endShape(CLOSE)
        
    def middle_blue_shape(self):
        # middle blue shape
        fill(64, 96, 165)
        stroke(64, 96, 165)
        beginShape()
        vertex(510, 213)
        vertex(737, 395)
        vertex(770, 395)
        vertex(770, 185)
        bezierVertex(750, 175, 715, 170, 715, 170)
        bezierVertex(722, 155, 720, 110, 690, 75)
        vertex(390, 175)
        vertex(315, 390)
        vertex(96, 560)
        vertex(195.1, 497.9)
        vertex(292.6, 497.9)
        vertex(292.6, 574.9)
        vertex(350, 574.9)
        endShape(CLOSE)
        
    def largest_navy_cloud(self):
        # largest navy cloud
        fill(51, 52, 90)
        stroke(51, 52, 90)
        beginShape()
        vertex(33, 185)
        bezierVertex(100, 18, 390, 15, 455, 100)
        bezierVertex(468, 5, 650, 12, 690, 75)
        bezierVertex(600, 130, 515, 185, 390, 175)
        bezierVertex(560, 177, 480, 330, 310, 390) #first half of 4th curve
        bezierVertex(290, 403, 110, 468, 34, 383) #second half of 4th curve
        bezierVertex(70, 362, 115, 365, 115, 368)
        bezierVertex(70, 350, 50, 315, 37, 290)
        bezierVertex(60, 275, 90, 252, 260, 280)
        bezierVertex(180, 274, 140, 253, 160, 220)
        bezierVertex(90, 235, 60, 210, 33, 185)
        endShape(CLOSE)
        
    def right_bottom_navy_shape(self):
        # right bottom navy shape 
        fill(51, 52, 90)
        stroke(51, 52, 90)
        beginShape()
        vertex(737, 395)
        bezierVertex(685, 450, 580, 450, 517, 403) 
        bezierVertex(610, 525, 740, 510, 770, 500)
        vertex(770, 395)
        endShape(CLOSE)
    
    def first_purple_triangle(self):
        # first purple triangle 
        fill(64, 96, 165)
        stroke(64, 96, 165)
        beginShape()
        vertex(0, 590.3)
        vertex(0, 550)
        vertex(102.7, 422)
        vertex(51.3, 590.3)
        endShape(CLOSE)
        
    def first_light_blue_triangle(self):
        # first light blue triangle
        fill(170, 204, 226)
        stroke(170, 204, 226)
        beginShape()
        vertex(51.3, 590.3)
        vertex(102.7, 422)
        vertex(96, 560)
        endShape(CLOSE)
        
    def second_light_blue_triangles(self):
        # second light blue triangles
        fill(170, 204, 226)
        stroke(170, 204, 226)
        beginShape()
        vertex(351, 574.9)
        vertex(508, 213)
        vertex(431, 470)
        vertex(545, 351)
        vertex(467.1, 477.4)
        endShape(CLOSE)
    
    def third_light_blue_triangle(self):
        # third light blue triangle
        fill(170, 204, 226)
        stroke(170, 204, 226)
        beginShape()
        vertex(628, 544.1)
        vertex(644, 503)
        vertex(637, 544.1)
        endShape(CLOSE)
        
    def fourth_light_blue_triangle(self):
        # fourth light blue triangle
        fill(170, 204, 226)
        stroke(170, 204, 226)
        beginShape()
        vertex(687.9, 625)
        vertex(687.9, 578)
        vertex(770, 505)
        vertex(770, 520)
        endShape(CLOSE)
        
    def last_blue_triangle(self):
        # last blue triangle 
        fill(64, 96, 165)
        stroke(64, 96, 165)
        beginShape()
        vertex(687.9, 625)
        vertex(770, 520)
        vertex(770, 625)
        endShape(CLOSE)
        
    def right_navy_cloud(self):
        # right navy cloud
        fill(51, 52, 90)
        stroke(51, 52, 90)
        beginShape()
        vertex(715, 170)
        bezierVertex(708, 195, 670, 210, 640, 213)
        bezierVertex(765, 205, 786, 345, 737, 395)
        bezierVertex(500, 405, 480, 265, 510, 213)
        bezierVertex(555, 124, 713, 165, 715, 170)
        endShape(CLOSE)

# create an instance of the Art class                                                                                                                                          
art = Art()

# invoke each of the drawing methods on the Art class to create the artwork
art.third_red_shape()
art.first_orange_shape()
art.first_red_shape()
art.first_yellow_triangle()
art.second_yellow_triangle()
art.third_yellow_triangle()
art.last_red_shape()
art.second_red_shape()
art.fifth_yellow_triangle()
art.sixth_yellow_triangle()
art.last_yellow_triangle()
art.last_orange_shape()
art.first_yellow_shape()
art.fourth_red_shape()
art.fourth_yellow_triangle()
art.second_orange_shape()
art.pale_yellow_fork_triangle()
art.navy_semicircle()
art.navy_left_boarder_semicircles()
art.top_blue_cloud()
art.middle_blue_shape()
art.largest_navy_cloud()
art.right_bottom_navy_shape()
art.first_purple_triangle()
art.first_light_blue_triangle()
art.second_light_blue_triangles()
art.third_light_blue_triangle()
art.fourth_light_blue_triangle()
art.last_blue_triangle()
art.right_navy_cloud()
