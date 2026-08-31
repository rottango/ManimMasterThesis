# the first node appears on the middle, like from 0 to 100% pop up style

# "Imagine, this is a robot"

# The first node is moved to the left
# The node then after some delay moves to the left and a node appears symetrically to it throguh the middle on the right the same way.

# "And this is the second robot."

# Then after some delay, they get arrows that show their axies XandY. Angle is added too between Y and X axis
# "In 2D space, they both have their orientations and angels"

# They rotate different directiojn, like a PID loop, tryig to localize each otehrs but they never manage.
# "But how can they locate each other, if neither of them know of the others existence?"

# Finished scene by a text appearing showin: How do robots localize each other? -> fade to black
# ACT 0 STARTS


from manim import *
from random import randrange

class openingSequence(Scene):
    def construct(self):
        
        # Create the nodes and axis
        node_1 = Circle(radius=1.5,
                        color=BLUE,
        )

        node_2 = Circle(radius=1.5,
                        color=RED)
                
        # Introdce nodes and Move them to the start position for adding axes
        self.play(Create(node_1), run_time=2.5)
        self.play(node_1.animate.set_fill(BLUE, opacity=0.7), run_time=1)
        # "Imagine, this is a robot"
        self.wait(2)

        self.play(
            node_1.animate.to_edge(UP, buff=1), node_1.animate.to_edge(LEFT, buff=1)
        )

        self.play(
            node_1.animate.scale(0.5), Succession(Wait(1), Create(node_2)), run_time=2.5
        )
        self.play(node_2.animate.set_fill(RED, opacity=0.7), run_time=1)
        # "And this is a second robot."

        self.wait(2)

        self.play(
            node_2.animate.to_edge(UP, buff=1),
            node_2.animate.to_edge(RIGHT, buff=1),
            node_1.animate.scale(2),
            run_time=2,
        )
        # "In 2D space, they both have their orientations and angels"
        # "But how can they locate each other, if neither of them know of the others existence?"
        
        # Create the axis in the center of the nodes
        x_axis_node_1 = Arrow(start=node_1.get_center(),
                             end=node_1.get_center()+RIGHT*2,
                             color=RED,
                             buff=0)
        x_axis_node_2 = Arrow(start=node_2.get_center(),
                             end=node_2.get_center()+RIGHT*2,
                             color=RED,
                             buff=0)

        y_axis_node_1 = Arrow(start=node_1.get_center(),
                             end=node_1.get_center()+UP*2,
                             color=BLUE,
                             buff=0)
        y_axis_node_2 = Arrow(start=node_2.get_center(),
                             end=node_2.get_center()+UP*2,
                             color=BLUE,
                             buff=0)
        
        node_1_axes=VGroup(x_axis_node_1,y_axis_node_1)
        node_2_axes=VGroup(x_axis_node_2,y_axis_node_2)

        self.play(Create(x_axis_node_1),Create(y_axis_node_1))
        self.play(Create(x_axis_node_2),Create(y_axis_node_2))
        self.wait(0.5)
        self.play(Rotate(node_2_axes,
                         PI,
                         about_point=node_2_axes[0].get_start()),run_time=1)
        self.wait(1)

        # Rotate the axis in a randomized  sequence
        #first rotation
        self.play(Rotate(node_1_axes,
                         -0.3* PI,
                         about_point=node_1_axes[0].get_start()),
                  Rotate(node_2_axes,
                         0.2*PI,
                         about_point=node_2_axes[0].get_start()),run_time=2)
        #second rotation
        self.play(Rotate(node_1_axes,
                         2*0.3* PI,
                         about_point=node_1_axes[0].get_start()),
                  Rotate(node_2_axes,
                         2*-0.4* PI,
                         about_point=node_2_axes[0].get_start()),run_time=1*2)
        #third rotation
        self.play(Rotate(node_1_axes,
                         -0.3*PI-0.7* PI,
                         about_point=node_1_axes[0].get_start()),
                  Rotate(node_2_axes,
                         2*0.6*PI,
                         about_point=node_2_axes[0].get_start()),run_time=1*2)
        #fourth rotation
        self.play(Rotate(node_1_axes,
                         2*0.7*PI,
                         about_point=node_1_axes[0].get_start()),
                  Rotate(node_2_axes,
                         -0.8*PI,
                         about_point=node_2_axes[0].get_start()),run_time=1*2)
        #fifth rotation
        self.play(Rotate(node_1_axes,
                         -0.7*PI-1*PI,
                         about_point=node_1_axes[0].get_start()),
                  Rotate(node_2_axes,
                         0.9*PI,
                         about_point=node_2_axes[0].get_start()),run_time=1*2)
        #sixth rotation
        self.play(Rotate(node_1_axes,
                         2*PI,
                         about_point=node_1_axes[0].get_start()),
                  Rotate(node_2_axes,
                         -0.7*PI,
                         about_point=node_2_axes[0].get_start()),run_time=1*2)


    def basicMovementofNodes(self, node_1, node_2):
        self.play(Create(node_1), run_time=2.5)
        self.play(node_1.animate.set_fill(BLUE, opacity=0.7), run_time=1)
        # "Imagine, this is a robot"
        self.wait(2)

        self.play(
            node_1.animate.to_edge(UP, buff=1), node_1.animate.to_edge(LEFT, buff=1)
        )

        self.play(
            node_1.animate.scale(0.5), Succession(Wait(1), Create(node_2)), run_time=2.5
        )
        self.play(node_2.animate.set_fill(RED, opacity=0.7), run_time=1)
        # "And this is a second robot."

        self.wait(2)

        self.play(
            node_2.animate.to_edge(UP, buff=1),
            node_2.animate.to_edge(RIGHT, buff=1),
            node_1.animate.scale(2),
            run_time=2,
        )
        # "In 2D space, they both have their orientations and angels"
        # "But how can they locate each other, if neither of them know of the others existence?"

    def createLines(self, node_1, node_2):
        x_axis_node_1 = Arrow(start=node_1.get_center(),
                             end=node_1.get_center()+RIGHT*2,
                             color=RED,
                             buff=0)
        x_axis_node_2 = Arrow(start=node_2.get_center(),
                             end=node_2.get_center()+RIGHT*2,
                             color=RED,
                             buff=0)

        y_axis_node_1 = Arrow(start=node_1.get_center(),
                             end=node_1.get_center()+UP*2,
                             color=BLUE,
                             buff=0)
        y_axis_node_2 = Arrow(start=node_2.get_center(),
                             end=node_2.get_center()+UP*2,
                             color=BLUE,
                             buff=0)
        
        node_1_axes=VGroup(x_axis_node_1,y_axis_node_1)
        node_2_axes=VGroup(x_axis_node_2,y_axis_node_2)

        self.play(Create(node_1_axes))
        self.play(Create(node_2_axes))
        self.wait(2)
                
        return node_1_axes,node_2_axes


    def createNodes(self):
        node_1 = Circle(
            radius=1.5,
            color=BLUE,
        )

        node_2 = Circle(radius=1.5, color=RED)
        return node_1, node_2
