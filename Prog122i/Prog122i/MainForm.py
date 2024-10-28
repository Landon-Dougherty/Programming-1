import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(21, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(714, 479)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.BurlyWood
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(21, 517)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(204, 96)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(274, 517)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(204, 96)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.BurlyWood
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(531, 517)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(204, 96)
        self._button3.TabIndex = 3
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveBorder
        self.ClientSize = System.Drawing.Size(903, 638)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog122i"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        header = "Number\t\t\tCube Root\t\t\tCube"
        self._listBox1.Items.Add(header)
        for num in range (-25,0):
            anum = abs(num)
            cuberoot = round(anum**(1/3.0),2)
            cube = num**3
            list = str(num) + "\t\t\t" + str(-cuberoot) + "\t\t\t" + str(cube)
            self._listBox1.Items.Add(list)  
        for num2 in range (0,26):
           cuberoot2 = round(num2**(1/3.0),2)
           cube2 = num2**3
           list2 = str(num2) + "\t\t\t" + str(cuberoot2) + "\t\t\t" + str(cube2)
           self._listBox1.Items.Add(list2)           



    def Button2Click(self, sender, e):
        Application.Exit()

    def Button3Click(self, sender, e):
        self._listBox1.Items.Clear()