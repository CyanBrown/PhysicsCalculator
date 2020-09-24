from kinematics import kinematics
from projectile import projectile


class handler:
    def __init__(self, V=None, V0=None, X=None, X0=None, T=None, A=None, from_vector=['x', 0, 0], round_to=3):
        self.values = {'V': V, 'V0': V0, 'X': X, 'X0': X0, 'T': T, 'A': A}
        self.from_vector = from_vector
        self.round_to = round_to
        self.handle()

    def handle(self):

        if self.from_vector[0] == 'x' and self.from_vector[1] + self.from_vector[2] != 0:
            self.values['V0'] = projectile.projectile.composite_vector(self.from_vector[1], self.from_vector[2])[0]
        elif self.from_vector[0] == 'y' and self.from_vector[1] + self.from_vector[2] != 0:
            self.values['V0'] = projectile.projectile.composite_vector(self.from_vector[1], self.from_vector[2])[1]
        elif self.from_vector[0] == 'projectile':
            self.x_vel, self.y_vel = projectile.composite_vector(self.from_vector[1], self.from_vector[2])
            self.values_y = {'X0': self.values['X0'], 'V0': self.y_vel, 'X': 0, 'A': -10, 'T': None, 'V': -self.y_vel}
            self.values_y = kinematics.calculate_attributes(self.values_y)
            print(self.values_y, 'this is the test from in handle')
            self.values_x = {'X0': self.values['X0'], 'V0': self.x_vel, 'X': None, 'A': 0, 'V': self.x_vel,
                             'T': self.values_y[0]['T']}
            self.values_x = kinematics.calculate_attributes(self.values_x)
            # self.values_X = {'V0':self.x_vel,'V':self.values['V0'],'A':0,'X0':0,'X':0}
        self.values = kinematics.calculate_attributes(self.values, self.round_to)
        return self.values

    def graph(self):
        print(self.values_y, 'fuck this')
        print(self.values_y, 'fuck this bitch')
        y_form = projectile.vals_to_time(self.values_y)
        print(self.values_y, 'after vals to time')
        print(y_form)
        x_form = projectile.vals_to_time(self.values_x)
        print(self.values_y, self.values_x)

        formula = y_form.replace('x', '(' + x_form + ')')
        print(x_form, 'yeet', y_form, 'yeet', formula)
        print(self.values_y[0]['T'])
        projectile.graph(y_form, x_to=self.values_y[0]['T'], y_l='X (Y values)')
        projectile.graph(x_form, x_to=self.values_x[0]['T'], y_l='X (X values)', title='Horizontal Distance to time')
        projectile.graph(formula, x_to=self.values_x[0]['X'], x_l='X (X distance)', y_l='X (Y distance)',
                         title='Vertical Distance to Horizontal Distance')
