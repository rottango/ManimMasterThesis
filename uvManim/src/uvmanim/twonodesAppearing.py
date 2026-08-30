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


class openingSequence(Scene):
    def construct(self):
        Node1, Node2 = self.createNodes()
        self.basicMovementofNodes(Node1, Node2)
        self.createLines(Node1,Node2)

    def basicMovementofNodes(self, Node1, Node2):
        self.play(Create(Node1), run_time=2.5)
        self.play(Node1.animate.set_fill(BLUE, opacity=0.7), run_time=1)
        # "Imagine, this is a robot"
        self.wait(2)

        self.play(
            Node1.animate.to_edge(UP, buff=1), Node1.animate.to_edge(LEFT, buff=1)
        )

        self.play(
            Node1.animate.scale(0.5), Succession(Wait(1), Create(Node2)), run_time=2.5
        )
        self.play(Node2.animate.set_fill(RED, opacity=0.7), run_time=1)
        # "And this is a second robot."

        self.wait(2)

        self.play(
            Node2.animate.to_edge(UP, buff=1),
            Node2.animate.to_edge(RIGHT, buff=1),
            Node1.animate.scale(2),
            run_time=2,
        )
        # "In 2D space, they both have their orientations and angels"
        # "But how can they locate each other, if neither of them know of the others existence?"

    def createLines(self, Node1, Node2):
        xAxisOfNode1 = Arrow(start=Node1.get_center(), end=Node1.get_center()+RIGHT*2, color=RED)
        xAxisOfNode2 = Arrow(start=Node2.get_center(), end=Node2.get_center()+RIGHT*2, color=RED)

        yAxisOfNode1 = Arrow(start=Node1.get_center(), end=Node1.get_center()+UP*2, color=BLUE)
        yAxisOfNode2 = Arrow(start=Node2.get_center(), end=Node2.get_center()+UP*2, color=BLUE)
        self.play(Create(xAxisOfNode1), Create(yAxisOfNode1))
        self.play(Create(xAxisOfNode2), Create(yAxisOfNode2))
        self.wait(10)


    def createNodes(self):
        Node1 = Circle(
            radius=1.5,
            color=BLUE,
        )

        Node2 = Circle(radius=1.5, color=RED)
        return Node1, Node2
